# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacity'
print 'U'+s[2:]

############################################

#1.32 Understanding Selection

# For any string,

s = 'supercalfragalisticexpialidocious'

print s[:]
# = s 

print s+s[0:-1+1] 
# = s 

print s[0:]
# = s 

print s[:-1]
# != s 

print s[:3]+s[3:]
# = s 

