t = int(input())
for i in range(t):
  n = int(input())
  
  flag = 0
  count = 0
  while n != 1:
    if n % 6 == 0:
      n /= 6
      flag = 0
      count += 1
    elif flag == 0:
      flag = 1
      n *= 2
      count += 1
    else:
      count = -1
      break
      
  print(count)