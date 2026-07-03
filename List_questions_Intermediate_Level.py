"""
9. Write a program to merge two lists and remove duplicates.

l1 = [25,45,36,85]
l2 = [56,4576,56,"sanjeev"]
l1.extend(l2)
print(l1)

10. Write a program to find common elements between two lists. 

li1 = [12,45,36,165465,456,45]
li2 = [465,46,68,56,12,45]
for i in li1:
    if i in li2:
        print(i)

11. Write a program to split a list into even and odd numbers

li1 = [56,456,13,468,156,654,31,45]
a = []
b = []
for i in li1:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)

print("List:",li1)
print("Even numbers are:",a)
print("Odd numbers are:",b)

12. Write a program to rotate a list by n positions.

li = [1,2,3,4,5,6,7,8,9,12,45]
n = int(input("How many times you want to rotate the list: "))
rotated_list = li[n:]+li[:n]

print("Original List:", li)
print("Rotated List:", rotated_list)

13. Write a Python program to find the second largest number in a list.

li = [5,65,543,786,34,465,456,456]
unq = list(set(li))
unq.sort()

sec_largest = unq[-2]

print("List with no duplicates:",unq)
print("Second Largest number:",sec_largest)

14. Write a program to flatten a nested list.

lists = [[12,45],[86,456],["sanjeev",456],[456,25]]
flat_list = []
for list in lists:
    for item in list:
        flat_list.append(item)
print("Original list:",lists)
print("Flatten list:",flat_list)

15. Write a program to count frequency of each element in a list.

list = [1,5,8,4,6,9,8,4,5,6,2,7,7,1]
fre = {}
for num in list:
    if num in fre:
        fre[num]=fre[num]+1
    else:
        fre[num]=1
print("List:",list)
print("Frequence of each elements:")

for key, value in fre.items():
    print(key,":",value)

16. Write a program to replace all negative numbers with zero in a list. 

list = [546,13,687,456,-45,46,-35,-45]
for i in range(len(list)):
    if list[i]<0:
        list[i]=0

print("Updated list:",list)
"""
