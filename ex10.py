"I am 6'2\" tall." # escape double-quote inside string
'I am 6\'2" tall.' # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# this is a lesson on escape sequences
# \\ will give you one backslash...
# so it looks like I'm \ a \ cat

# \" Double quote (")
# \' Single quote (')
# \n new line
# \t tab
# \a ASCII Bell (BEL) Bell warning
# \b ASCII Backspace (BS)
# \f ASCII Formfeed (FF) page break
# \N{name} Character named name in the Unicode database (Unicode only)
# \r ASCII Carriage Return (CR)
# \uxxxx Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx I(Unicode only)
# v\ ASCII Vertical Tab (VT)
# \ooo Character with octal value ooo
# \xhh Character with hex value hh
