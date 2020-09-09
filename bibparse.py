import re

ENTRY_FIRST_LINE = re.compile(r'^\s*@\w+{(.*),\s*$')
ENTRY_LAST_LINE = re.compile(r'^\s*}\s*$')

def has_content(line: str) -> bool:
    for c in line:
        if c == '%':
            # Commented line, ignore
            return False
        elif not c.isspace():
            # Contains non-whitespace character
            return True
    # Does not contain any non-whitespace characters
    return False

def is_entry_first_line(line: str) -> bool:
    return ENTRY_FIRST_LINE.match(line) is not None

def is_entry_last_line(line: str) -> bool:
    return ENTRY_LAST_LINE.match(line) is not None

def split_entries(lines: list) -> list:
    entries = []
    entry = []
    in_entry = False
    for line in lines:
        if has_content(line):
            if line[-1] == '\n':
                # Trim newline
                line = line[:-1]
            if in_entry:
                entry.append(line)
                if is_entry_last_line(line):
                    in_entry = False
                    entries.append(entry)
                    entry = []
            elif is_entry_first_line(line):
                    in_entry = True
                    entry.append(line)
    if in_entry:
        raise Exception('Last bib entry not closed?')
    return entries

def entry_key(entry: list) -> str:
    return ENTRY_FIRST_LINE.match(entry[0]).group(1)
