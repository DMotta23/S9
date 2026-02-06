import random

#write a function that adds 10 random numbers

sum_num = 0
for i in range(10):
    sum_num += random.randint(1, 100)
print(sum_num)