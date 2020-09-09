#!/usr/bin/env python3

if __name__ != "__main__":
    raise Exception('Main script imported')

import sys
from bibparse import split_entries, entry_key

# Read lines
lines = None
if len(sys.argv) < 2:
    lines = sys.stdin.readlines()
elif len(sys.argv) == 2:
    with open(sys.argv[1], mode='r') as fd:
        lines = fd.readlines()
else:
    print('Usage: bibdup [BIB_FILE]')
    exit()
# Read entries
entries = split_entries(lines)
# Print duplicate entry keys
visited = set()
for entry in entries:
    key = entry_key(entry)
    if key in visited:
        print(key)
    else:
        visited.add(key)
