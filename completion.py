"""
Çift amaçlı:
1) Bash completion:  python3 completion.py <COMP_WORDS...>
2) Help :            python3 completion.py --help
"""

import sys, os, textwrap
from structure import options, positionals

# ───────────────────────── HELP MOD ─────────────────────────
if len(sys.argv) <= 1 or sys.argv[1] in ("-h", "--help"):
    def render(opt_dict, indent=0):
        pad = "  " * indent
        for k, meta in opt_dict.items():
            desc = meta.get("description", "")
            default = meta.get("default", None)
            line = f"{pad}{k:<16} : {desc}"
            if default not in (None, "", [], False):
                line += f" (default: {default})"
            print(textwrap.fill(line, subsequent_indent=pad + "  ", width=90))
            if meta.get("type") == "group":
                print(f"{pad}  Sub-arguments:")
                render(meta["sub"], indent + 2)

    print("\nes2panda – Available options\n" + "-" * 35)
    render(options)

    if positionals:
        print("\nPositional arguments:")
        for pos in positionals:
            line = f"  {pos['name']:<16} : {pos['description']}"
            if pos.get("required"):
                line += " (required)"
            print(textwrap.fill(line, subsequent_indent=" " * 20, width=90))

    sys.exit(0)

# ─────────────────── COMPLETION MOD ───────────────────
args = sys.argv[1:]
cur  = args[-1] if args else ""
prev = args[-2] if len(args) > 1 else ""
prev2= args[-3] if len(args) > 2 else ""

def match(items):
    for item in items:
        if str(item).startswith(cur):
            print(item)

# 1. … xxx yyy <TAB> → List sub values
if prev2 in options and options[prev2].get("type") == "group":
    submap = options[prev2]["sub"]
    if prev in submap:
        typ = submap[prev]["type"]
        if typ == "file":
            match(os.listdir("."))
        elif typ == "list":
            match(submap[prev]["values"])
        sys.exit(0)

# 2. … xxx <TAB> → List sub keys
if prev in options and options[prev].get("type") == "group":
    match(options[prev]["sub"].keys())
    sys.exit(0)

# 3. File completion
if prev in options and options[prev]["type"] == "file":
    match(os.listdir("."))
    sys.exit(0)

# 4. List completion
if prev in options and options[prev]["type"] == "list":
    match(options[prev]["values"])
    sys.exit(0)

# 5. Positional completion (If the first argument is file)
if not any(a.startswith("--") for a in args):
    for pos in positionals:
        if pos["type"] == "file":
            match(os.listdir("."))
            sys.exit(0)

# 6. Top-level options
match(options.keys())

