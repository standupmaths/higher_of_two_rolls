from random import randint

number_of_sides = int(input("How many sides on your dice? "))
trials = 10**6
sum_of_results = sum(max(randint(1, number_of_sides), randint(1, number_of_sides)) for _ in range(trials))

print(f"Average result of rolling two and taking the highest is about {sum_of_results/trials}")
