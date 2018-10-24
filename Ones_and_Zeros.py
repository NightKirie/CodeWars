def binary_array_to_number(arr):
  expo = len(arr) - 1
  total = 0
  for num in arr: 
      if num is 1:
          total = total + pow(2, expo)
      expo = expo - 1
  return total    
