
a =  input("enter the list of numbers seperating by comma :", ).split(',')
print(a)
result = map(lambda x:int(x)*3,a)
print(list(result))
