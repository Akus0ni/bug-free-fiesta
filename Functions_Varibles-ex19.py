def cheese_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" %cheese_count
	print "You have %d crackers!" %boxes_of_crackers
	print "Man thats enoung for a party!"
	print "Get a blanket.\n"
	

print "We can just give function numbers directly:"
cheese_crackers(20,30)

print"OR, we can use variable from our script: "
amt_cheese = 10
amt_crackers = 50

cheese_crackers(amt_cheese,amt_crackers)


print "We can even do math inside too: "
cheese_crackers(10+20, 5*6)

print "And we can combine the two variables and math: "
cheese_crackers(amt_cheese+100, amt_crackers*0.5)