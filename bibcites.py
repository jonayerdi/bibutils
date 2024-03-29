#!/usr/bin/env python3

if __name__ != "__main__":
    raise Exception('Main script imported')

import sys
import re

CITATION = re.compile(r'\\cite{([\w\s,]*)}')

# Read text
text = None
if len(sys.argv) < 2:
    text = sys.stdin.read()
elif len(sys.argv) == 2:
    with open(sys.argv[1], mode='r', encoding='utf-8') as fd:
        text = fd.read()
else:
    print('Usage: bibcites <BIB_FILE>')
    exit()
# Find and print distinct citations
visited = set()
for match in CITATION.finditer(text):
    citations = match.group(1)
    for citation in citations.split(','):
        citation = citation.strip()
        if citation not in visited:
            visited.add(citation)
for citation in sorted(visited):
    print(citation)
