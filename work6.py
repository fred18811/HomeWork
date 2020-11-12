from itertools import count
from itertools import cycle

for i in count(10):
	print(i)
	if i == 15:
		break


count_val = 0
for i in cycle("SPAM"):
	if count_val > 7:
	   break
	print(i)
	count_val += 1
