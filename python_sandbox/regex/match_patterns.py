""" Test pattern matching
"""

import re


def match_table_names(tables, pattern):
    r = re.compile(pattern)
    return filter(r.match, tables)


if __name__ == '__main__':
    # should print ['abc', 'abcd', 'abcdef', 'abc_moe']
    tables = ['abc', 'abcd', 'abcdef', 'moe_abc', 'moe_abcdef', 'abc_moe']
    pattern = 'abc.*'
    print match_table_names(tables, pattern)
