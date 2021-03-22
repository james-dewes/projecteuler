f1 = 1
f2 = 2
f3 = 0
total = 2

while f3 < 3999999:
	f3 = f1 + f2
	f1 = f2
	f2 = f3
	if f3 % 2 == 0:
		total += f3
	
print total

