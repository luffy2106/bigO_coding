"""
1. Question
You recently wrote a random number generator code for a web application and now you notice that some cracker has cracked it. It now gives numbers at a difference of some given value k more predominantly. You being a hacker decide to write a code that will take in n numbers as input and a value k and find the total number of pairs of numbers whose absolute difference is equal to k, in order to assist you in your random number generator testing.

NOTE: All values fit in the range of a signed integer, n, k>=1

Input
1st line contains n & k.
2nd line contains n numbers of the set. All the n numbers are assured to be distinct.

(Edited: n <= 10^5)

Output
One integer saying the number of pairs of numbers that have a diff k.

Ex :

Input:
5 2
1 5 3 4 2
Output:
3

Explain : We can see that there are 3 pairs which have diff k = 2: (1,3), (5,3), (4,2)


Source :

https://www.spoj.com/problems/HACKRNDM/

(this problem come from lecture binary search but you can also solve the problem by BST as well)
https://bigocoder.com/courses/138/lectures/1843/problems/1076?view=statement

2. Solution
- We can see that this problem can be seen as seaching number problem, with the number need to be searched is 
1. num + k
2. num - k

num is each element in the input list

To be able to search a number using binary search, we need to sort it first(Binary search ONLY WORK for SORTTED array.)

"""


def binary_search(left, right, a, target):
    if left <= right:
        mid = (left + right) //2
        if a[mid] == target:
            return True
        else:
            if a[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            return binary_search(left,right,a,target)
    return False


def count_pais_with_different_k(a, k):
    left = 0
    right = len(a)-1
    count = 0
    for num in a:
        target_bigger = num + k
        target_smaller = num - k
        if binary_search(left, right, a , target_bigger):
            count+=1
        if binary_search(left, right, a , target_smaller):
            count+=1
    # Because during the loop each pair will be count twice : (3,1) and (1,3) is the same, so we need to divide by 2
    count = count // 2
    return count
    
n, k = 5,2
a = [1,5,3,4,2]
a.sort()

print(count_pais_with_different_k(a,k))
    
