#!/usr/bin/env python3
"""
Çift amaçlı:
1) Bash completion:  python3 completion.py <COMP_WORDS...>
"""

import sys, os, textwrap
from structure import options  # aynı klasördeki metadata


# COMPLETION MOD (CALLS BASH)
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

