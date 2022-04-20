x=("apple", "banana", "cherry")
print(type(x))
print(x)

2+3

2%8

8%2


x={"name" : "John", "age" : 36}
print(x, type(x))


x=True
print(x, type(x));


x=20.5
y=7.8
z= x-y
print(z, type(z))


x= range(6)
print(x, type(x))


x= bytearray(5)
print(x, type(x))


x=5
x=float(x)
print(x)


x=5.0
x=complex(x)
print(x)

x="Urvashi here"
print(len(x))

txt="Urvashi Prajapati"
x=txt[4]
print(x)

txt = "Hello World"
x= txt[2:5]
print(x)

txt="  Urvashi here"
x=txt.strip()
print(x)

txt = "Hello World"
txt=txt.upper()
print(txt)

txt="Hello World"
txt = txt.replace("Hello", "Happy")
print(txt)

txt="Hello World"
txt= txt.replace("H", "J")
print(txt)

age=22
txt="My name is Urvi, and I am {}"
print(txt.format(age))

print(10>9)

print(99<78)

print(9==8)

print(bool("abc"))

print(10 * 5)

fruits = ["cherry", "grapes"]
if "apple" in fruits: print("Yes, apple is a fruit!")

if 5 == 10 or 4 == 4: print("At least one of the statements is true")

fruits = ["apple", "banana", "cherry"]

fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi"
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

fruits = ["apple", "banana", "cherry"]
print(fruits[0])

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car.get("year"))


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]= "red"
print(car.get("color"))


a = 50
b = 10
if a== b: print("Yes")
else: print("No")


a = 50
b = 10
if a== b: print("1")
elif a> b: print("2")
else: print("3")


a= 60
b= 70
c= 90
d= 90
if a == b and c == d: print("Hello")


if a == b or c == d: print("Hello")


print("Yes") if 5 > 2 else print("No")


if 5 > 2:
  print("Five is greater than two!")

if 5 > 2: print("Five is greater than two!")

i = 1
while i < 6:
  print(i)
  i += 1



i=1
while i < 6:
    if i == 3:
    break
    i += 1
    print(i)

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
print(i)

