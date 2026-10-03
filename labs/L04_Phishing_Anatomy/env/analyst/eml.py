#!/usr/bin/env python3
"""
eml.py - print the facts stored in a saved email message.

Reads an RFC 5322 message file (.eml) and prints what is actually in it:
the addresses, the delivery path, the authentication results the receiving
server recorded, the links, and the attachments.

It renders nothing and it judges nothing. There is no "suspicious" verdict in
this program, because deciding that is the analyst's job and the whole point of
the exercise. Every line it prints is copied or decoded from the file.

Usage:
  eml.py FILE                      summary: who, what, when, and what's inside
  eml.py --headers FILE            the full delivery path and auth results
  eml.py --links FILE              every link, with the text it was shown as
  eml.py --attachments FILE        attachment names, types, sizes, SHA-256
  eml.py --attachments --save DIR FILE    also write the decoded bytes out
  eml.py --raw FILE                the raw header block, unmodified

Options combine: `eml.py --headers --links FILE` prints both sections.
Only Python's standard library is used, so this runs anywhere Python 3 does.
"""

import argparse
import hashlib
import pathlib
import sys
from email import message_from_bytes, policy
from email.header import decode_header, make_header
from html.parser import HTMLParser

RULE = "-" * 72


def unfold(value):
    """Header continuation lines arrive back as embedded tabs/newlines.

    Split them out again so a long Received line is readable on screen
    instead of scrolling off the right-hand edge.
    """
    text = str(value).replace("\r\n", "\n").replace("\t", "\n")
    return [part.strip() for part in text.split("\n") if part.strip()]


# --------------------------------------------------------------------------- utils
def decode(value):
    """Header values may be RFC 2047-encoded. Show the readable form."""
    if value is None:
        return None
    try:
        return str(make_header(decode_header(value)))
    except Exception:
        return value


def load(path):
    try:
        return message_from_bytes(pathlib.Path(path).read_bytes(),
                                  policy=policy.default)
    except FileNotFoundError:
        sys.exit(f"eml.py: no such file: {path}\n"
                 f"        (inside the container the messages are in /cases/)")


def section(title):
    print()
    print(title)
    print(RULE)


class AnchorCollector(HTMLParser):
    """Collect (href, visible text) pairs from an HTML body."""

    def __init__(self):
        super().__init__()
        self.anchors = []
        self._href = None
        self._text = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self.anchors.append((self._href, "".join(self._text).strip()))
            self._href = None
            self._text = []


def bodies(msg):
    """Yield (content_type, text) for every non-attachment body part."""
    for part in msg.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get_content_disposition() == "attachment":
            continue
        try:
            yield part.get_content_type(), part.get_content()
        except Exception:
            payload = part.get_payload(decode=True) or b""
            yield part.get_content_type(), payload.decode("utf-8", "replace")


def attachments(msg):
    """Yield (filename, declared_type, decoded_bytes) for each attachment."""
    for part in msg.walk():
        if part.get_content_disposition() != "attachment":
            continue
        data = part.get_payload(decode=True) or b""
        yield (part.get_filename() or "(no filename)",
               part.get_content_type(), data)


# ------------------------------------------------------------------------ sections
def print_summary(msg, path):
    section(f"SUMMARY  {path}")
    for field in ("From", "Reply-To", "Return-Path", "To", "Cc",
                  "Subject", "Date", "Message-ID", "In-Reply-To", "X-Mailer"):
        value = msg.get(field)
        if value:
            print(f"  {field+':':<14}{decode(value)}")

    auth = msg.get("Authentication-Results")
    if auth:
        print(f"  {'Auth results:':<14}(see --headers for the full record)")

    hops = msg.get_all("Received") or []
    print(f"  {'Received:':<14}{len(hops)} hop(s)   (see --headers)")

    link_count = 0
    for ctype, text in bodies(msg):
        if ctype == "text/html":
            collector = AnchorCollector()
            collector.feed(text)
            link_count += len(collector.anchors)
    print(f"  {'Links:':<14}{link_count}          (see --links)")

    atts = list(attachments(msg))
    print(f"  {'Attachments:':<14}{len(atts)}          (see --attachments)")
    for name, ctype, data in atts:
        print(f"                 - {name}  [{ctype}]  {len(data)} bytes")


def print_headers(msg):
    section("DELIVERY PATH  (Received headers)")
    hops = msg.get_all("Received") or []
    if not hops:
        print("  (none recorded)")
    else:
        print("  Each server prepends its own line, so the LAST line below is the")
        print("  earliest hop and the FIRST line is the most recent. Read bottom-up")
        print("  to follow the message forward through the network.")
        print()
        for i, hop in enumerate(hops, start=1):
            label = "most recent" if i == 1 else ("earliest" if i == len(hops) else "")
            print(f"  [{i}] {label}")
            for line in unfold(hop):
                print(f"      {line}")
            print()

    section("AUTHENTICATION RESULTS  (as recorded by the receiving server)")
    auth = msg.get("Authentication-Results")
    if not auth:
        print("  (no Authentication-Results header present)")
    else:
        for line in unfold(auth):
            print(f"  {line}")
    print()
    print("  Reminder of what each check is for:")
    print("    SPF   - was this sending server permitted to send for the")
    print("            envelope domain? (Return-Path, not necessarily From.)")
    print("    DKIM  - is there a valid signature, and which domain signed it?")
    print("    DMARC - does the From domain line up with an SPF or DKIM pass,")
    print("            and what did that domain ask receivers to do on failure?")

    sig = msg.get("DKIM-Signature")
    if sig:
        print()
        print("  A DKIM-Signature is present. The signing domain is the d= value:")
        for field in str(sig).replace("\n", " ").split(";"):
            field = field.strip()
            if field.startswith(("d=", "s=")):
                print(f"      {field}")


def print_links(msg):
    section("LINKS  (href, and the text it was displayed as)")
    found = False
    for ctype, text in bodies(msg):
        if ctype != "text/html":
            continue
        collector = AnchorCollector()
        collector.feed(text)
        for href, shown in collector.anchors:
            found = True
            print(f"  shown as : {shown or '(no visible text)'}")
            print(f"  goes to  : {href}")
            print()
    if not found:
        print("  (no HTML links found; if the body is plain text, read it directly)")


def print_attachments(msg, save_dir):
    section("ATTACHMENTS")
    atts = list(attachments(msg))
    if not atts:
        print("  (none)")
        return
    for name, ctype, data in atts:
        print(f"  filename       : {name}")
        print(f"  declared type  : {ctype}")
        print(f"  decoded size   : {len(data)} bytes")
        print(f"  sha256         : {hashlib.sha256(data).hexdigest()}")
        if save_dir:
            out = pathlib.Path(save_dir) / name
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(data)
            print(f"  written to     : {out}")
            print(f"                   (view it as TEXT - e.g. `cat {out}` -")
            print(f"                    never by opening it in a browser)")
        print()


def print_raw(msg):
    section("RAW HEADER BLOCK")
    for line in str(msg)[:str(msg).find("\n\n")].splitlines():
        print(f"  {line}")


# ----------------------------------------------------------------------------- main
def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=(
            "Print the facts stored in a saved email message.\n\n"
            "It renders nothing and it judges nothing. There is no 'suspicious'\n"
            "verdict in this program, because deciding that is the analyst's job.\n"
            "Every line it prints is copied or decoded from the file."),
        epilog=("With no section flags, prints the summary. Flags combine:\n"
                "  eml --headers --links FILE   prints both sections."))
    parser.add_argument("file", help="path to a .eml file")
    parser.add_argument("--headers", action="store_true",
                        help="delivery path and authentication results")
    parser.add_argument("--links", action="store_true",
                        help="every link, with the text it was shown as")
    parser.add_argument("--attachments", action="store_true",
                        help="attachment names, types, sizes and SHA-256")
    parser.add_argument("--save", metavar="DIR",
                        help="with --attachments, write the decoded bytes to DIR")
    parser.add_argument("--raw", action="store_true",
                        help="the raw header block, unmodified")
    args = parser.parse_args()

    if args.save and not args.attachments:
        sys.exit("eml.py: --save only means something with --attachments")

    msg = load(args.file)
    chose = args.headers or args.links or args.attachments or args.raw

    if not chose:
        print_summary(msg, args.file)
    if args.headers:
        print_headers(msg)
    if args.links:
        print_links(msg)
    if args.attachments:
        print_attachments(msg, args.save)
    if args.raw:
        print_raw(msg)
    print()


if __name__ == "__main__":
    main()
