cars = 100 #No. of cars
space_in_a_car = 4.0 #No. Of Seats in a cars
drivers= 30 #no. of drivers
passengers = 90 # no of passengers
cars_not_driven = cars-drivers #no of idle cars
cars_driven = drivers #No of cars not idle
carpool_capacity = cars_driven * space_in_a_car #no of seats available in non idle cars
average_passengers_per_car = passengers / cars_driven


print "There are ", cars, "cars available."
print "There are only ",drivers, "drivers availble."
print "There will be ", cars_not_driven, " empty cars today."
print "We can transport ", carpool_capacity, "people today."
print "We have ", passengers, " to carpool today."
print "We need to put about ", average_passengers_per_car, " in each car."