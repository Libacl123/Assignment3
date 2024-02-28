def swap(var_one, var_two):
  

    return var_two, var_one 

var_one = 'a'
var_two = 1

var_one, var_two = swap(var_one, var_two)  

print(f"var_one = {var_one}, var_two = {var_two}") 
