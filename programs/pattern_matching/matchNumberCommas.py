#! python3
# matchNumberCommas.py - finds numbers in comma case format

import re

commaCaseRegex = re.compile(r'''(
    ^\d{1,3}(,\d{3})*$

    )''', re.VERBOSE)

match = commaCaseRegex.search('123,124,123,234,123')

print(match.group())
