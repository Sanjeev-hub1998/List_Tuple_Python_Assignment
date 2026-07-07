"""
35. Write a program to find the index of an element in a tuple. 

t = int(input("Enter the number present in tuple:"))
t1 = (45,25,68,45,36,456,12,8,48,5,6,7)
if t in t1:
    print("element",t,"is at",t1.index(t),"position")
else:
    print("Element not available!")

36. Write a program to remove an element from a tuple (without directly modifying it).

t = int(input("Enter the removing element: "))
t1 = (45,5,8,6,3,54,8,100)
if t in t1:
    t2 = list((t1))
    print("Is element",t,"exist in tuple?:",t2.remove(t))
else:
    print("Element",t,"not available in Tuple!")

37. Write a program to find common elements between two tuples. 

t1 = (45,5,8,6,45,25,86,132)
t2 = (15,5,86,3,4,698,4,2,82,8,45)
t3 = set((t1))
t4 = set((t2))
print("Common elements are:",t3.intersection(t4))

38. Write a Python program to check if a tuple is a palindrome.

t = (1,2,3,4,3,2,1)
if t==t[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")

39. Write a program to find the element with maximum frequency in a tuple.

t = (5,5,2,7,7,5,8,8,9,2,2)

max_element = t[0]
max_count = t.count(t[0])
for i in t:
    if t.count(i)>max_count:
        max_count=t.count(i)
        max_element=i
        
print("Tuple:", t)
print("Element with maximum frequency:", max_element)
print("Frequency:", max_count)

40. Write a program to create a nested tuple and access its elements.

t = (2,5,8,3,(5,8,6,"sanjeev",5,True),12,8)
print(t)
print("Nested elements are:",t[4])


"""
li = [1,5,8,6,4,8,36,4,7,5,7,5]
fre = []
for i in li:
    if i not in fre:
        count = li.count(i)
        print("Frequency",count,":",[i]*count)
        fre.append(i)