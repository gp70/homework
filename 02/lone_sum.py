def lone_sum(a, b, c):
  sum = a + b + c
  if a==b:
    sum = sum - 2*a
  if b==c:
    sum = sum - 2*b
  if a==c:
    sum = sum - 2*c
  if a==b==c:
    sum = 0
  return sum
