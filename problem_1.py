counter = 0
three = 0
while counter < 999:
	counter = counter + 1
	if counter % 3 == 0:
		three = three + counter


counter = 0
five = 0
while counter < 999:
	counter = counter + 1
	if counter % 5 == 0:
		five = five + counter

minus = 0
counter = 0
while counter < 999:
	counter = counter + 1
	if counter % 15 == 0:
		minus = minus + counter		

print three
print five
print minus

print three + five - minus	

counter = 0
total = 0
while counter < 999:
	counter = counter + 1
	if counter % 3 == 0 or counter % 5 == 0:
		total = total + counter


print total
