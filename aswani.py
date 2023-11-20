x=5
y="jhon"
print(x)
print(y)
myvar="jhon"
my_var="jhon"
myvar1="jhon"
myvar="jhon"
MYVAR="jhon"
x,y,z="orange","apple","cherry"
print(x)
print(y)
print(z)
x=y=z="orange"
print(x)
print(y)
print(z)
fruits=["apple","orange","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)
import random
print(random.randrange(1,10))
a="hello"
print(a)
print(a[1])
print(a[2])
print(a[0])
print(len(a))
b="   hello ,hii world"
print("is" in b)
print(b[:6])
print(b[10:])
print(b[5:9])
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("o","w"))
print(b.split(","))
a="hi"
b="friends"
c=a+" "+b
print(c)
text="I love apples,apples are my favorite"
a=text.count("apple")
print(a)
x="banana"
y=x.center(20)
print(y)
print(10>9)
print(5<3)
print(bool("hii"))
print(bool())
a=5
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)

fru=["apple","orange","pappaya","grapes"]
newlist=[]
for x in fru:
    if "g" in x:
        newlist.append(x)
print(newlist)

newone=[x for x in fru if "g" in x]
print(newone)

new=[x for x in range(20,50) if x<25]
print(new)

a = 2
b = 4
x=[a,b]
x.sort(reverse=True)
print(x[0])


if "apple" in fru:
    print("yes")
else:
    print("no")

animal=["cow","goat","lion","tiger"]
for i in range(len(animal)):
 print(animal[i])

i=0
while i<len(animal):
 print(animal[i])
 i=i+1

