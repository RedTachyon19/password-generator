import random
n = random.randint(16,20)
array = [' '] * n

for i in range (n):
	while array[i] == ' ':
		array[i] = chr(random.randint(41,127))
	print(array[i], end = '')
