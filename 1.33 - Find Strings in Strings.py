
pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of spheres.'

print pythagoras.find('humming')
#25

print pythagoras[25:]
#humming of the strings...

print pythagoras.find('T')
#0 

print 'test'.find('t')
#0 

print "test".find('st')
#2

print "Test".find('te')
#-1 - not found 

print 'west'.find('test')
#-1 - not found 

print "test"[-1]
#t 

############# 1.36 - Finding with Numbers

danton = "De l'audace, encore de l'audace, toujours de l'audace."

print danton.find('audace')
#5
print danton.find('audace', 0)
#5
print danton.find('audace', 5)
#5
print danton.find('audace', 6)
#25
print danton[6:]
#udace, encore de l'audace, toujours de l'audace.
print danton.find('audace', 26)
#47
