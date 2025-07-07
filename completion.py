#!/usr/bin/env python3
"""
Çift amaçlı:
1) Bash completion:  python3 completion.py <COMP_WORDS...>
2) Help :  python3 completion.py --help
"""

import sys, os, textwrap
from structure import options  # aynı klasördeki metadata

# ─────────────────────────  HELP MODU  ─────────────────────────
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
    sys.exit(0)

# ───────────────────  COMPLETION MOD (CALLS BASH) ───────────────────
args = sys.argv[1:]
cur  = args[-1] if args else ""
prev = args[-2] if len(args) > 1 else ""
prev2= args[-3] if len(args) > 2 else ""

def match(items):  # filter + writed
    for item in items:
        if str(item).startswith(cur):
            print(item)

# 1. … xxx yyy <TAB>   (List sub values)
if prev2 in options and options[prev2].get("type") == "group":
    submap = options[prev2]["sub"]
    if prev in submap:
        typ = submap[prev]["type"]
        if typ == "file":
            match(os.listdir("."))
        elif typ == "list":
            match(submap[prev]["values"])
        # bool / int -> öneri gerekmez
        sys.exit(0)

# 2. … xxx <TAB>  (List sub keys)
if prev in options and options[prev].get("type") == "group":
    match(submap := options[prev]["sub"].keys())
    sys.exit(0)

# 3. File Completion
if prev in options and options[prev]["type"] == "file":
    match(os.listdir("."))
    sys.exit(0)

# 4. Options for static lists
if prev in options and options[prev]["type"] == "list":
    match(options[prev]["values"])
    sys.exit(0)

# 5. Top level options (flags)
match(options.keys())

