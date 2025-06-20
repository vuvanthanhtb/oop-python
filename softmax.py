import math

val_1 = 1.0
val_2 = 2.0
val_3 = 3.0

total = math.exp(val_1) + math.exp(val_2) + math.exp(val_3)

softmax_1 = math.exp(val_1) / total
softmax_2 = math.exp(val_2) / total
softmax_3 = math.exp(val_3) / total

print(f"Softmax of {val_1} is {softmax_1:.5f}")
print(f"Softmax of {val_2} is {softmax_2:.5f}")
print(f"Softmax of {val_3} is {softmax_3:.5f}")
