# Defining a string on multiple lines, using triple quotes and the line continuation character ( \ )
my_string = '''this\
is\
my\
first\
string'''

# Strings - indexing
a = "Cisco Switch"

a.index("i")

# Strings - character count
a = "Cisco Switch"

a.count("i")

# Strings - finding a character
a = "Cisco Switch"

a.find("sco")

# Strings - converting the case
a = "Cisco Switch"

a.lower()  # lowercase

a.upper()  # uppercase

# Strings - checking whether the string starts with a character
a = "Cisco Switch"

a.startswith("C")

# Strings - checking whether the string ends with a character
a = "Cisco Switch"

a.endswith("h")

# Strings - removing a character from the beginning and the end of a string
a = "   Cisco Switch   "

a.strip()  # remove whitespaces

b = "$$$Cisco Switch$$$"

b.strip("$")  # remove a certain character

# Strings - removing all occurences of a character from a string
a = "   Cisco Switch   "

a.replace(" ", "")  # replace each space character with the absence of any character

# Strings - splitting a string by specifying a delimiter; the result is a list
a = "Cisco,Juniper,HP,Avaya,Nortel"  # the delimiter is a comma

a.split(",")

# Strings - inserting a character in between every two characters of the string / joining the characters by using a delimiter
a = "Cisco Switch"

"_".join(a)

# Additional methods (source: https://www.tutorialspoint.com/python3/python_strings.htm)

capitalize()
# Capitalizes first letter of string.

lstrip()
# Removes all leading whitespace in string.

rstrip()
# Removes all trailing whitespace of string.

swapcase()
# Inverts case for all letters in string.

title()
# Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

isalnum()
# Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

isalpha()
# Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

isdigit()
# Returns true if string contains only digits and false otherwise.

islower()
# Returns true if string has at least 1 cased character an