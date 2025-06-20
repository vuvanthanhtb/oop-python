import math

val_1 = 1.0
val_2 = 2.0
val_3 = 3.0

max_val = max(val_1, val_2, val_3)

e_v1 = math.exp(val_1 - max_val)
e_v2 = math.exp(val_2 - max_val)
e_v3 = math.exp(val_3 - max_val)

total = e_v1 + e_v2 + e_v3

softmax_1 = e_v1 / total
softmax_2 = e_v2 / total
softmax_3 = e_v3 / total

print(f"Softmax of {val_1} is {softmax_1:.5f}")
print(f"Softmax of {val_2} is {softmax_2:.5f}")
print(f"Softmax of {val_3} is {softmax_3:.5f}")
