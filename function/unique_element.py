def lst(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(lst([1,1,2,2,2,5,5,8,8,0,0]))