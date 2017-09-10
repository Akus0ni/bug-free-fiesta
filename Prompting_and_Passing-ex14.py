from sys import argv

script, u_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." %(u_name, script)
print "I'd like to ask you a few questions."
print "Do u like me %s?" %u_name
likes = raw_input(prompt)

print "Where do u live %s?" %u_name
lives = raw_input(prompt)

print "What kind of computer do u have?"
computer = raw_input(prompt)

print """
Alright, so u said %r about liking me.
You live in %r. Not sure where that is.
And u have a %r computer. Nice.
""" %(likes, lives, computer)