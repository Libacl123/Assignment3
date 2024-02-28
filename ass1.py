def assign(values):
  large = max(values)
  small = min(values)

  return large, small

values = [45, 56, 98, 3, 67, 9, 90]

large, small = assign(values)

print(f"Largest number is {large}, Smallest number is {small}.")  
