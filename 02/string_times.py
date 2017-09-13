def string_times(str, n):
  if n==0:
    return ''
  if n==1:
    return str
  return str + string_times(str, n-1)
