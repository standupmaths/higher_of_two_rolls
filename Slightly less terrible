from random import randint
from statistics import mean

number_of_sides  =  int(input("How many sides on your dice? "))

avg =  mean([max(randint(1,number_of_sides), randint(1,number_of_sides)) for _ in range(10**6)])

print(f"Average result of rolling two and taking the highest is about {avg}")
