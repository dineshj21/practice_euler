num_sq_total = 0
num_sum = 0
for i in range (1,101):
    num_sq_total += i*i
    num_sum += i

sq_sum = num_sum * num_sum
result = sq_sum - num_sq_total
print(result)
