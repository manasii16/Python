# Merge Strings Alternatively-Leetcode
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result=[]
        i=0
        while i<len(word1) or i<len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i+=1
        return ''.join(result)

# ------------------------------------------------------------------------------------------------------------------
# Divide array into arrays with Max difference 
# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.


class Solution(object):
    def divideArray(self, nums, k):
        v=[]           # Create an empty vector to store the divided sub-arrays
        nums.sort()    #Sort the input nums in ascending order

        for i in range(len(nums)-2):
            if i%3 == 0:
                if nums[i+2]-nums[i] <= k:   #Calculate the difference between the third and first elements subarray  
                    v.append([nums[i],nums[i+1],nums[i+2]])
                else:
                    return []
        return v
--------------------------------------------------------------------------------------------------------------------------
# Max Difference You Can Get From Changing an Integer
# You are given an integer num. You will apply the following steps exactly two times:

# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# The new integer cannot have any leading zeros, also the new integer cannot be 0.
# Let a and b be the results of applying the operations to num the first and second times, respectively.

# Return the max difference between a and b.

class Solution(object):
    def maxDiff(self, num):
        a=b=str(num)
        for digit in a:
            if digit!="9":
                a=a.replace(digit,"9")
                break
        if b[0]!="1":
            b=b.replace(b[0],"1")
        else:
            for digit in b[1:]:
                if digit not in "01":
                    b=b.replace(digit,"0")
                    break
        return int(a)-int(b)
        
--------------------------------------------------------------------------------------
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true
# if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        i = 0
        
        while i<length:
            if flowerbed[i]==0:
               next=flowerbed[i+1] if i<length-1 else 0
               if next ==0:
                    n-=1
                    i+=2
               else:
                i+=1
               if n==0:
                return True
            else:
                i+=2
        return n<=0

--------------------------------------------------------------------------------------------------------------------------------------------
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution(object):
    def reverseVowels(self, s):
        
        # Convert the input string to a character array.
        arr = list(s)
        
        start = 0
        end = len(s) - 1
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        # Loop until the start pointer is no longer less than the end pointer.
        while start < end:
            
            if s[start] not in vowels:
                start+=1
                
            if s[end] not in vowels:
                end-=1
                
            if s[start] in vowels and s[end] in vowels:
                
                # Swap the vowels found at the start and end positions.
                arr[start], arr[end] = arr[end], arr[start]
            
                # Move the pointers towards each other for the next iteration.
                start += 1
                end -= 1
        
        # Convert the character array back to a string and return the result.
        return "".join(arr)
    
    
    
        
