##### 2.2

# Write Python code that prints out the number of hours in 7 weeks.

print 7*7*24
# 1176

##### 2.6 Bodacious Udacity

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print s[:2]+t[3:]
# udacious

##### 2.7

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo" 

# ENTER CODE BELOW HERE

print text.find('hoo')
# 6

##### 2.8 Find 2 
#Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.
text = "all zip files are zipped"
first_zip = text.find('zip')
second_zip = text.find('zip', first_zip +1)
print second_zip

#OR
first_zip = text.find('zip')
print text.find('zip', first_zip +1)

#OR
print text.find('zip', text.find('zip')+1)


##### 2.9 Rounding Numbers

# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159

#ENTER CODE BELOW HERE
print round(3.14159)

print round(2.5)
print round(1.4)
print round(3.5)









