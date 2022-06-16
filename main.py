result = []
def divider(a, b):
 if a < b:
  raise ValueError
 if b > 100:
  raise IndexError
 return a/b
try:
 data = (10/2 , 2 / 5 ,123 / 4, 18 / 0, [] / 15 , 8  / 4)
except ZeroDivisionError:
  print("There is ZeroDivisionError in your code!")
except NameError:
 print("There is NameError in your code!")
 for key in data:
  res = divider(key, data[key])
  result.append(res)

print(result)