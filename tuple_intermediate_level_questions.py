"""
29. Write a program to slice a tuple and display the result. 

t = (45,25,45,8,69,75,63,"sanjeev","vikas",12)
print(t[4:8])
print(t[-6:-2])

30. Write a program to find repeated elements in a tuple. 

t = (1,5,3,7,8,9,12,45,45,8,6,3,3)
repeated = []
for i in t:
    if t.count(i)>1 and i not in repeated:
        repeated.append(i)
print("Tuple:",t)
print("Repeated elements are:",repeated)

31. Write a program to merge two tuples. 

t1 = (45,25,78,36)
t2 = ("sanjeev","vikas","vijay","neeraj")
t3 = tuple(list(zip(t1,t2)))
print(t3)

32. Write a program to unpack elements of a tuple into variables.

student = ("sanjeev",20,"Ghaziabad")
name,age,city = student
print("name:",name)
print("age:",age)
print("city:",city)

33. Write a Python program to sort a tuple

t = (45,25,13,1,5,8,99,456)
li = list(t)
li.sort()
print(tuple(li))

34. Write a program to convert a list of tuples into a dictionary. 


"""
data = [("name","sanjeev"),("age",20),("city","Ghaziabad")]
d = dict(data)
print("Dictionary:",d)