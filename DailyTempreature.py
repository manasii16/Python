# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
# is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)

        # store days until a warmer temperature, initialized with zeros
        result=[0]*n
        stack=[]

        for i in range(n-1,-1,-1):
            
            # For each temperature, pop elements from the stack until a warmer temperature is found.
            while stack and temperatures[stack[-1]]<=temperatures [i]:
                stack.pop()
            
            if stack:
                result[i]=stack[-1]-i
            
            # Push the current index onto the stack.
            stack.append(i)
        return result
