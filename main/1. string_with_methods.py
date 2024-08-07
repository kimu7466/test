string_name = "my name is IMROZ khan"

# all_string_method = dir(string_name)

# all_methods =[]

# for i in all_string_method :
#     if i.startswith("__") :
#         pass
#     else:
#         all_methods.append(i)

# # print(all_methods)

# for ind , i in enumerate(all_methods) :
#     print(f"{ind+1} : {i}")
# print(help(str))
# print(string_name.casefold())

"""
1 : capitalize - 
2 : casefold
3 : center
4 : count
5 : encode
6 : endswith
7 : expandtabs
8 : find
9 : format
10 : format_map
11 : index
12 : isalnum
13 : isalpha
14 : isascii
15 : isdecimal
16 : isdigit
17 : isidentifier
18 : islower
19 : isnumeric
20 : isprintable
21 : isspace
22 : istitle
23 : isupper
24 : join
25 : ljust
26 : lower
27 : lstrip
28 : maketrans
29 : partition
30 : removeprefix
31 : removesuffix
32 : replace
33 : rfind
34 : rindex
35 : rjust
36 : rpartition
37 : rsplit
38 : rstrip
39 : split
40 : splitlines
41 : startswith
42 : strip
43 : swapcase
44 : title
45 : translate
46 : upper
47 : zfill
"""
def print_help():
    x = """
    Help on class str in module builtins:

    class str(object)
    |  str(object='') -> str
    |  str(bytes_or_buffer[, encoding[, errors]]) -> str
    |
    |  Create a new string object from the given object. If encoding or
    |  errors is specified, then the object must expose a data buffer
    |  that will be decoded using the given encoding and error handler.
    |  Otherwise, returns the result of object.__str__() (if defined)
    |  or repr(object).
    |  encoding defaults to sys.getdefaultencoding().
    |  errors defaults to 'strict'.
    |
    |  Methods defined here:
    |
    |  __add__(self, value, /)
    |      Return self+value.
    ||
    ||
    ||
    ||
    || {IMROZ KHAN REMOVED ALL DUNDER METHODS }
    ||
    ||
    ||
    |  capitalize(self, /)
    |      Return a capitalized version of the string.
    |
    |      More specifically, make the first character have upper case and the rest lower
    |      case.
    |
    |  casefold(self, /)
    |      Return a version of the string suitable for caseless comparisons.
    |
    |  center(self, width, fillchar=' ', /)
    |      Return a centered string of length width.
    |
    |      Padding is done using the specified fill character (default is a space).
    |
    |  count(...)
    |      S.count(sub[, start[, end]]) -> int
    |
    |      Return the number of non-overlapping occurrences of substring sub in
    |      string S[start:end].  Optional arguments start and end are
    |      interpreted as in slice notation.
    |
    |  encode(self, /, encoding='utf-8', errors='strict')
    |      Encode the string using the codec registered for encoding.
    |
    |      encoding
    |        The encoding in which to encode the string.
    |      errors
    |        The error handling scheme to use for encoding errors.
    |        The default is 'strict' meaning that encoding errors raise a
    |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
    |        'xmlcharrefreplace' as well as any other name registered with
    |        codecs.register_error that can handle UnicodeEncodeErrors.
    |
    |  endswith(...)
    |      S.endswith(suffix[, start[, end]]) -> bool
    |
    |      Return True if S ends with the specified suffix, False otherwise.
    |      With optional start, test S beginning at that position.
    |      With optional end, stop comparing S at that position.
    |      suffix can also be a tuple of strings to try.
    |
    |  expandtabs(self, /, tabsize=8)
    |      Return a copy where all tab characters are expanded using spaces.
    |
    |      If tabsize is not given, a tab size of 8 characters is assumed.
    |
    |  find(...)
    |      S.find(sub[, start[, end]]) -> int
    |
    |      Return the lowest index in S where substring sub is found,
    |      such that sub is contained within S[start:end].  Optional
    |      arguments start and end are interpreted as in slice notation.
    |
    |      Return -1 on failure.
    |
    |  format(...)
    |      S.format(*args, **kwargs) -> str
    |
    |      Return a formatted version of S, using substitutions from args and kwargs.
    |      The substitutions are identified by braces ('{' and '}').
    |
    |  format_map(...)
    |      S.format_map(mapping) -> str
    |
    |      Return a formatted version of S, using substitutions from mapping.
    |      The substitutions are identified by braces ('{' and '}').
    |
    |  index(...)
    |      S.index(sub[, start[, end]]) -> int
    |
    |      Return the lowest index in S where substring sub is found,
    |      such that sub is contained within S[start:end].  Optional
    |      arguments start and end are interpreted as in slice notation.
    |
    |      Raises ValueError when the substring is not found.
    |
    |  isalnum(self, /)
    |      Return True if the string is an alpha-numeric string, False otherwise.
    |
    |      A string is alpha-numeric if all characters in the string are alpha-numeric and
    |      there is at least one character in the string.
    |
    |  isalpha(self, /)
    |      Return True if the string is an alphabetic string, False otherwise.
    |
    |      A string is alphabetic if all characters in the string are alphabetic and there
    |      is at least one character in the string.
    |
    |  isascii(self, /)
    |      Return True if all characters in the string are ASCII, False otherwise.
    |
    |      ASCII characters have code points in the range U+0000-U+007F.
    |      Empty string is ASCII too.
    |
    |  isdecimal(self, /)
    |      Return True if the string is a decimal string, False otherwise.
    |
    |      A string is a decimal string if all characters in the string are decimal and
    |      there is at least one character in the string.
    |
    |  isdigit(self, /)
    |      Return True if the string is a digit string, False otherwise.
    |
    |      A string is a digit string if all characters in the string are digits and there
    |      is at least one character in the string.
    |
    |  isidentifier(self, /)
    |      Return True if the string is a valid Python identifier, False otherwise.
    |
    |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
    |      such as "def" or "class".
    |
    |  islower(self, /)
    |      Return True if the string is a lowercase string, False otherwise.
    |
    |      A string is lowercase if all cased characters in the string are lowercase and
    |      there is at least one cased character in the string.
    |
    |  isnumeric(self, /)
    |      Return True if the string is a numeric string, False otherwise.
    |
    |      A string is numeric if all characters in the string are numeric and there is at
    |      least one character in the string.
    |
    |  isprintable(self, /)
    |      Return True if the string is printable, False otherwise.
    |
    |      A string is printable if all of its characters are considered printable in
    |      repr() or if it is empty.
    |
    |  isspace(self, /)
    |      Return True if the string is a whitespace string, False otherwise.
    |
    |      A string is whitespace if all characters in the string are whitespace and there
    |      is at least one character in the string.
    |
    |  istitle(self, /)
    |      Return True if the string is a title-cased string, False otherwise.
    |
    |      In a title-cased string, upper- and title-case characters may only
    |      follow uncased characters and lowercase characters only cased ones.
    |
    |  isupper(self, /)
    |      Return True if the string is an uppercase string, False otherwise.
    |
    |      A string is uppercase if all cased characters in the string are uppercase and
    |      there is at least one cased character in the string.
    |
    |  join(self, iterable, /)
    |      Concatenate any number of strings.
    |
    |      The string whose method is called is inserted in between each given string.
    |      The result is returned as a new string.
    |
    |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    |
    |  ljust(self, width, fillchar=' ', /)
    |      Return a left-justified string of length width.
    |
    |      Padding is done using the specified fill character (default is a space).
    |
    |  lower(self, /)
    |      Return a copy of the string converted to lowercase.
    |
    |  lstrip(self, chars=None, /)
    |      Return a copy of the string with leading whitespace removed.
    |
    |      If chars is given and not None, remove characters in chars instead.
    |
    |  partition(self, sep, /)
    |      Partition the string into three parts using the given separator.
    |
    |      This will search for the separator in the string.  If the separator is found,
    |      returns a 3-tuple containing the part before the separator, the separator
    |      itself, and the part after it.
    |
    |      If the separator is not found, returns a 3-tuple containing the original string
    |      and two empty strings.
    |
    |  removeprefix(self, prefix, /)
    |      Return a str with the given prefix string removed if present.
    |
    |      If the string starts with the prefix string, return string[len(prefix):].
    |      Otherwise, return a copy of the original string.
    |
    |  removesuffix(self, suffix, /)
    |      Return a str with the given suffix string removed if present.
    |
    |      If the string ends with the suffix string and that suffix is not empty,
    |      return string[:-len(suffix)]. Otherwise, return a copy of the original
    |      string.
    |
    |  replace(self, old, new, count=-1, /)
    |      Return a copy with all occurrences of substring old replaced by new.
    |
    |        count
    |          Maximum number of occurrences to replace.
    |          -1 (the default value) means replace all occurrences.
    |
    |      If the optional argument count is given, only the first count occurrences are
    |      replaced.
    |
    |  rfind(...)
    |      S.rfind(sub[, start[, end]]) -> int
    |
    |      Return the highest index in S where substring sub is found,
    |      such that sub is contained within S[start:end].  Optional
    |      arguments start and end are interpreted as in slice notation.
    |
    |      Return -1 on failure.
    |
    |  rindex(...)
    |      S.rindex(sub[, start[, end]]) -> int
    |
    |      Return the highest index in S where substring sub is found,
    |      such that sub is contained within S[start:end].  Optional
    |      arguments start and end are interpreted as in slice notation.
    |
    |      Raises ValueError when the substring is not found.
    |
    |  rjust(self, width, fillchar=' ', /)
    |      Return a right-justified string of length width.
    |
    |      Padding is done using the specified fill character (default is a space).
    |
    |  rpartition(self, sep, /)
    |      Partition the string into three parts using the given separator.
    |
    |      This will search for the separator in the string, starting at the end. If
    |      the separator is found, returns a 3-tuple containing the part before the
    |      separator, the separator itself, and the part after it.
    |
    |      If the separator is not found, returns a 3-tuple containing two empty strings
    |      and the original string.
    |
    |  rsplit(self, /, sep=None, maxsplit=-1)
    |      Return a list of the substrings in the string, using sep as the separator string.
    |
    |        sep
    |          The separator used to split the string.
    |
    |          When set to None (the default value), will split on any whitespace
    |          character (including \n \r \t \f and spaces) and will discard
    |          empty strings from the result.
    |        maxsplit
    |          Maximum number of splits.
    |          -1 (the default value) means no limit.
    |
    |      Splitting starts at the end of the string and works to the front.
    |
    |  rstrip(self, chars=None, /)
    |      Return a copy of the string with trailing whitespace removed.
    |
    |      If chars is given and not None, remove characters in chars instead.
    |
    |  split(self, /, sep=None, maxsplit=-1)
    |      Return a list of the substrings in the string, using sep as the separator string.
    |
    |        sep
    |          The separator used to split the string.
    |
    |          When set to None (the default value), will split on any whitespace
    |          character (including \n \r \t \f and spaces) and will discard
    |          empty strings from the result.
    |        maxsplit
    |          Maximum number of splits.
    |          -1 (the default value) means no limit.
    |
    |      Splitting starts at the front of the string and works to the end.
    |
    |      Note, str.split() is mainly useful for data that has been intentionally
    |      delimited.  With natural text that includes punctuation, consider using
    |      the regular expression module.
    |
    |  splitlines(self, /, keepends=False)
    |      Return a list of the lines in the string, breaking at line boundaries.
    |
    |      Line breaks are not included in the resulting list unless keepends is given and
    |      true.
    |
    |  startswith(...)
    |      S.startswith(prefix[, start[, end]]) -> bool
    |
    |      Return True if S starts with the specified prefix, False otherwise.
    |      With optional start, test S beginning at that position.
    |      With optional end, stop comparing S at that position.
    |      prefix can also be a tuple of strings to try.
    |
    |  strip(self, chars=None, /)
    |      Return a copy of the string with leading and trailing whitespace removed.
    |
    |      If chars is given and not None, remove characters in chars instead.
    |
    |  swapcase(self, /)
    |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
    |
    |  title(self, /)
    |      Return a version of the string where each word is titlecased.
    |
    |      More specifically, words start with uppercased characters and all remaining
    |      cased characters have lower case.
    |
    |  translate(self, table, /)
    |      Replace each character in the string using the given translation table.
    |
    |        table
    |          Translation table, which must be a mapping of Unicode ordinals to
    |          Unicode ordinals, strings, or None.
    |
    |      The table must implement lookup/indexing via __getitem__, for instance a
    |      dictionary or list.  If this operation raises LookupError, the character is
    |      left untouched.  Characters mapped to None are deleted.
    |
    |  upper(self, /)
    |      Return a copy of the string converted to uppercase.
    |
    |  zfill(self, width, /)
    |      Pad a numeric string with zeros on the left, to fill a field of the given width.
    |
    |      The string is never truncated.
    |
    |  ----------------------------------------------------------------------
    |  Static methods defined here:
    |
    |  __new__(*args, **kwargs) from builtins.type
    |      Create and return a new object.  See help(type) for accurate signature.
    |
    |  maketrans(...)
    |      Return a translation table usable for str.translate().
    |
    |      If there is only one argument, it must be a dictionary mapping Unicode
    |      ordinals (integers) or characters to Unicode ordinals, strings or None.
    |      Character keys will be then converted to ordinals.
    |      If there are two arguments, they must be strings of equal length, and
    |      in the resulting dictionary, each character in x will be mapped to the
    |      character at the same position in y. If there is a third argument, it
    |      must be a string, whose characters will be mapped to None in the result.

    None
    """

    print(x)


print_help()