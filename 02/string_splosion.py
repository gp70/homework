def string_splosion(str):
  n = 0
  nstr = ''
  while n in range(len(str)):
    nstr = nstr + str[0:n+1]
    n = n + 1
  return nstr
