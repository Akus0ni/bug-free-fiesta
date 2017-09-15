def add(a,b):
	print "Adding %d + %d" %(a,b)
	return a+b
	
def substract(a,b):
	print "Substracting %d - %d" %(a,b)
	return a-b
	
def multiply(a,b):
	print "Multi %d * %d" %(a,b)
	return a*b
	
def divide(a,b):
	print "Divide %d / %d" %(a,b)
	return a/b
	
age = add(30,5)
height = substract(77,3)
weight = multiply(37,2)
iq = divide(100,2)

print "age: %d, height: %d, weight: %d, iq: %d" %(age,height,weight,iq)

#a puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight,divide(iq,2))))

print "That becomes: ", what, "can u do it by hand?"
