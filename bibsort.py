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
    print('Usage: bibsort <BIB_FILE>')
    exit()
# Read and sort entries
entries = split_entries(lines)
entries.sort(key=entry_key)
# Print entries
for entry in entries:
    for line in entry:
        print(line)
