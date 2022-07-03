import random
import math 

number_of_side1  =  int(input("How many sides on dice 1? "))
number_of_side2  =  int(input("How many sides on dice 2? "))
print()
print("Input rolling method")
print("0: single dice")
print("1: highest of two")
print("2: lowest of two")
print("3: sum of two")
print("4: difference of two")
print("5: product of two")
method=int(input())
print()
exp=int(input("Input number of dice rolls 10^"))

results = []
sum_of_results = 0.0
maxi=0
result = 0

trials = 0
while trials < 10**exp:
	if method==1:
		result = max([int(random.random()*number_of_side1)+1,int(random.random()*number_of_side2)+1])
	elif method==2:
		result = min([int(random.random()*number_of_side1)+1,int(random.random()*number_of_side2)+1])
	elif method==3:
		result = (int(random.random()*number_of_side1)+1)+(int(random.random()*number_of_side2)+1)
	elif method==4:
		result = abs((int(random.random()*number_of_side1)+1)-(int(random.random()*number_of_side2)+1))
	elif method==5:
		result = (int(random.random()*number_of_side1)+1)*(int(random.random()*number_of_side2)+1)
	else:
		result = int(random.random()*number_of_side1)+1
	
	maxi = max(maxi,result)
	sum_of_results += result
	results.append(result)
	trials += 1

print(f"The average result is about {sum_of_results/trials}")

ordered = [0]*(maxi+1)

for result in results:
	ordered[result] += 1

maxi = 0
result = 0	
for number in ordered:
	print(f"{result:03d} occured {number} times with a probability of {number*100/trials}%")
	maxi = max(maxi, number)
	result += 1

result = 0	
for number in ordered:
	boxes = int(number*50/maxi)
	box = 0
	str = f"{result:03d}: "
	while box < boxes:
		str += "#"
		box += 1
	
	print(str)
	result += 1