#!/usr/bin/env python3

if __name__ != "__main__":
    raise Exception('Main script imported')

import sys
from bibparse import split_entries, entry_key

def usage():
    print('Usage: bibextract [-c|--check] <BIB_FILE>')
    exit()

# Read lines
if len(sys.argv) not in (2, 3):
    usage()
bibfile = sys.argv[1]
check = False
if len(sys.argv) == 3:
    if sys.argv[1] in ('-c', '--check'):
        bibfile = sys.argv[2]
    elif sys.argv[2] not in ('-c', '--check'):
        usage()
    check = True
lines = None
keys = [line.strip() for line in sys.stdin.readlines()]
with open(bibfile, mode='r') as fd:
    lines = fd.readlines()
# Read entries
entries = { entry_key(entry): entry for entry in split_entries(lines) }
# Print relevant entries
for key in keys:
    entry = entries.get(key)
    if entry is not None:
        for line in entry:
            print(line)
    elif check:
        print(f'Entry "{key}" not found')
        exit()
