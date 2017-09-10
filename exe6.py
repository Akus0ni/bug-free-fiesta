 # - -coding: utf- 8 - 
# WARNING! Remember to put # - -coding: utf- 8 - - at the top if you use nonASCII
# characters and get an encoding error.
x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print x
print y
# We use %r for debugging, since it displays the “raw” data of the variable,
# but we use %s and others for displaying to users
print "I said: %r." %x # string inside string
print "I also said: '%s'." %y # string inside string

hilarious = False
joke_eval = "Isn't that joke so funny?! %r"
print joke_eval %hilarious

w = "This is the left side of..." # string inside string
e= "a string with a right side." # string inside string

print w+e
