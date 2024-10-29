#Find out common letters between two strings Using Python

'''def common_letter():
    str1 = input("Enter 1st no: ")
    str2 = input("Enter 2nd no: ")
    s1 = set(str1)
    s2 = set(str2)
    lst= s1 & s2
    print(lst)

common_letter()'''

#Count the frequency of words appearing in a string Using Python

'''def words():
    str=input("Enter the sentence: ")
    li = str.split()
    d={}

    for i in li:
       d[i] = d.get(i,0)+1
    print(d)
words()'''

#Conversion of two list into Dictionary

'''List1 = [1,2]
List2 = ["Pune", "Mumbai"]
a = dict(zip(List1,List2))
print(a)

# Dictionary into Tuple
s = {1: 'Pune', 2: 'Mumbai'}
for i in s.items():
    print(i)'''

#FIND MISSING NUMBER IN AN ARRAY

'''def get_missing_summation(a):
    n = a[-1]
    sum1 = 0
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total-sum1)
a = [1, 2, 4, 5, 6, 7]
get_missing_summation(a)'''

#Find Out Pairs with given sum in an array

'''def twonum(arr,sum):
    arr.sort()
    left = 0
    right = len(arr)-1
    while (left<=right):
        if (arr[left]+arr[right]>sum):
            right=right-1
        elif (arr[left]+arr[right]<sum):
            left=left+1
        elif (arr[left]+arr[right]==sum):
            print("Values are", arr[left],"&", arr[right])
            right = right - 1
            left = left + 1

arr = [5,7,4,3,9,8,19,21]
sum = 17
twonum(arr,sum)'''