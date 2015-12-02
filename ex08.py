formatter = "%r %r %r %r"

#don't forget to put things within quotation marks!

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# there are no quotes around True and False.  Python recognizes them as keywords
# putting quotes around them will turn them into strings and it won't work right.
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing." ,
	"So I said goodnight."
)
