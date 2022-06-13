class Solution:
    def isValid(self, s: str) -> bool:
        # The idea of the solution of this problem, is to first create a dicionary to store the (key:value) pairs
        # and to create a stack to store the unmatched brackets
        # when looping through s, 
        # if char in s in the dic.values(), first store the values in the stack
        # then check if char in s is in the dictionary keys or not, 
        # if char in the dic.keys(), but the stack is empty, or dic[char] is not the same as stack.pop()
        # which means there is not a value to match with the key
        # then return false
        # at the end, return if the stack is empty or not

        dic = {'}':'{', ']':'[', ')':'('}
        stack = []

        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack == [] or dic[char] != stack.pop(): # means there is a key, but not a matching value
                    return False
            else:
                return False
        return stack == []

    # https://leetcode.com/problems/valid-parentheses/

    