"""

17. Write a program to remove all occurrences of a given element from a list.

li = [45,1,6,8,65,5,8,8,35,5,46,25]
updated_list = list(set(li))
print("Original list:",li)
print("Updated list:",updated_list)

18. Write a program to check if a list is a palindrome. 

numbers = [1,2,3,4,3,2,1]
if numbers==numbers[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

19. Write a Python program to find missing numbers in a given list of consecutive integers.

numbers = [1,3,4,6,8,9]
missing = []
for num in range(min(numbers),max(numbers)+1):
    if num not in numbers:
        missing.append(num)
print("Original list:",numbers)
print("Missing numbers:",missing)

20. Write a program to perform element-wise addition of two lists.

li1 = [12,36,15,25]
li2 = [1,8,465,36]
result = []
for i in range(len(li1)):
    result.append(li1[i]+li2[i])
print("Two list addition is",result)

22. Write a program to group elements based on frequency.  

li = [1,5,8,6,4,8,36,4,7,5,7,5]
fre = []
for i in li:
    if i not in fre:
        count = li.count(i)
        print("Frequency",count,":",[i]*count)
        fre.append(i)
"""
