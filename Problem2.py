def evenFibSum(limit):
  a, b = 0, 1
  evenSum = 0
  
  while(b < limit):
    temp = a
    a = b
    if a % 2 == 0:
      evenSum += a
    b = temp + b
  
  return evenSum
  
print(evenFibSum(4000000))
