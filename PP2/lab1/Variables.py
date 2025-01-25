x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
# неправильные: 2myvar = "John"
# my-var = "John"
# my var = "John"
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
x = 5
y = 10
print(x + y)
x = 5
y = "John"
print(x, y)
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)