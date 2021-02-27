for n in "banana":
    print(n)

# array more strict than a list, but order is impt
# for x in [1,2,3]:
    #print(x)

# is equal to for x in "banana":
    #print(x)

# is equal to for x in ["b","a","n","a","n","a"]:

#slicing strings

#using in as a logical operator
fruit = "banana"
if "n" in "banana":
    print("n")
#if n in banana, it will give  n

#lower/upper case string > lower(), upper()
greet = "HELLO BOB"
zap = greet.lower()
print(zap)

#search and replace

#stripping whitespace, lstrip(), rstrip()
white = "     hello sam"
result = white.lstrip()
print(result)

#prefixes, case sensitive
line = "Please have a nice day"
if line.startswith("Please"):
    print("starts with please")
#will give true if please is inside

sentence = "have a nice saturday"
if sentence.startswith("saturday"):
    print("yes")

#tuple is a single point within vector field. needs to begin with ()

# /n indicates a new line