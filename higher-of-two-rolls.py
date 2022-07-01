import random

number_of_sides  =  int(input("How many sides on your dice? "))

sum_of_results = 0.0

trials = 0
while trials < 10**6:
    sum_of_results += max([int(random.random()*number_of_sides)+1,int(random.random()*number_of_sides)+1])
    trials += 1

print("Average result of rolling two and taking the highest is about {0}".format(sum_of_results/trials))



