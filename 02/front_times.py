def front_times(str, n):
  str = str[0:3]
  if n==0:
    return ''
  if n==1:
    return str
  return str + front_times(str, n-1)
