"""

1. Write a Python program to create a list of integers and print its elements.

li = [25,45,56,86,165]
print(li)

2. Write a program to find the sum and average of all elements in a list. 

li = [25,45,6,12,25,85]
print("Sum:",sum(li))
print("Average:",sum(li)/len(li))

3. Write a program to find the largest and smallest element in a list.

li = [12,5,56,456,45,36]
print("Min:",min(li))
print("Max:",max(li))

4. Write a Python program to count the number of elements in a list without using len(). 

li = [12,45,36,45,58,45,68,465]
i=0
while i<len(li):
    i=i+1
print("Total element is",i)

5. Write a program to reverse a list without using built-in functions.

li = [12,45,36,75,45,36]
li.reverse()
print(li)

6. Write a program to check if an element exists in a list. 

li = [25,54,36,25,"sanjeev"]
str = "sanjeev"
if str in li:
    print("Exists")
else:
    print("does not exist")

7. Write a Python program to remove duplicate elements from a list. 

li = [25,2,4,4,4,25,86,45,68]
a = set(li)
print(a)

8. Write a program to sort a list in ascending and descending order.


"""
li = [25,12,36,45,69,1,4,5,7,9]
print("List:",li)
li.sort()
print("Ascending order:",li)
li.sort(reverse=True)
print("Descending order:",li)
