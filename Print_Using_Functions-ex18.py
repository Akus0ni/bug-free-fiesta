#this one is like ur scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1,arg2)
	
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" %(arg1,arg2)

# this just takes one arg
def print_one(arg1):
	print "arg1: %r" %arg1

# this one takes no args
def print_none():
	print "I got nothing.."
	

print_two("Aku","Soni")
print_two_again("Akash","Soni")
print_one("First!")
print_none()	