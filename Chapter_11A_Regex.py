#Regular Expressions
#In computing, a regular expression, also referred to as "regex" or "regexp",
#provides a concise and flexible means for matching strings of text, such
# as particular characters, words, or patterns of characters. A regular expression
# is written in a formal langauge that can be interpreted by a regular expression processor.
 
#Regular Expressions - Really clever "wild card" expressions for matching and parsing strings

#Understanding Regular Expresssions
#Very powerful and quite cryptic
#fun once you understand them
#Regular Expressions are a langauge unto themselves
#A lanaguage of "marker characters"-programming with characters
#It is kind of an "old school" langauge-compact

#Regular expression Quick Guide
# ^ Matches the beginning of a line
# $ Matches the end of the line
# . Matches any character
# \s Matches whitespace
# \S Matches any non-whitespace character
# * Repeats a character zero or more times
# *? Repeats a character zero or more times(non-greedy)
# + Repeats a character one or more times
# +? Repeats a character one or more times(non-greedy)
# [aeiou] Matches a single character in the listed set
# [^XYZ] Matches a single character not in the listd set
# [a-z0-9] The set of characters can include a range
# ( Indicates where string extraction is to start
# ) Indicates where string extraction is to end

#The reguar Expression Module
#Before you can use regular expressions in your program, you must import the library using "import re"

#You can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings

#You can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing: var[5:10]

#Using find()
#hand=open('mbox1.txt')
#for line in hand:
#    line=line.rstrip()
#    if line.find('From')    >=0:
#        print(line)

#Using re.search()
#import re

#hand=open('mbox1.txt')
#for line in hand:
#    line=line.rstrip()
#    if re.search('From',line):
#        print(line)

#Using startswith()
#hand=open('mbox1.txt')
#for line in hand:
#    line=line.rstrip()
#    if line.startswith('From'):
#        print(line)
#we fine-tune is matched by adding special characters to the string
#Wild-Card Charaters
#The dot character matches any character
#If you add the asterix character, the character is "any number of times"

# X-Sieve: CMU Sieve 2.3
# X-DSPAM-Result: Innocent
# X-DSPAM-Confidence: 0.8475
# X-Content-Type-Message-Body: text/plain

# ^X.*: where ^ is used to Match the start of the line, . is used to Match any character, * is Many times

#Fine-Tuning Your Match
#Depending on how "clean" your data is and the purpose of your application, you may want to narrow your match down a bit
# X-Sieve: CMU Sieve 2.3
# X-DSPAM-Result: Innocent
# X-Plane is behind schedule: two weeks
# ^X-\S+: where ^ is use to Match the start of the line, \ is sued to Match any non-whitespace cahracter, + is One or more times
