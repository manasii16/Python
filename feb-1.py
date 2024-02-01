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
