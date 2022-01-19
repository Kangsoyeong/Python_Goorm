answer = input()

total = 0
current = 1

for i in range(len(answer)):
	if answer[i] == 'O':
		total += current
		current += 1
	elif answer[i] == "X":
		if current > 1:
			current = 1

print(total)