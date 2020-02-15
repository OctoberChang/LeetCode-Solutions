#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def evalRPN(self, tokens):
        stack = []
        op = ['+', '-', '*', '/']
        for t, s in enumerate(tokens):
            if s in op:
                y, x = stack.pop(), stack.pop()
                if s == '+':
                    stack.append(x+y)
                elif s == '-':
                    stack.append(x-y)
                elif s == '*':
                    stack.append(x*y)
                elif s == '/':
                    stack.append(int(x/float(y)))
            else:
                stack.append(int(s))

        return stack.pop()


m = Solution()
tokens = ["4","-2","/","2","-3","-","-"]
print tokens, m.evalRPN(tokens)
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print tokens, m.evalRPN(tokens)
