def string_bits(str):
  n = 0
  nstr = ''
  while n in range(len(str)):
    nstr = nstr + str[n]
    n = n + 2
  return nstr
