class Solution:
    def isValid(self, s: str) -> bool:
    #def isValid(self, s):
        # Number # 1
        # stack = []
        # pairs = {
        #     '(':')',
        #     '{':'}',
        #     '[':']'
        # }
        # for bracket in s:
        #     if bracket in s: 
        #         stack.append(bracket)
        #     elif len(stack) == 0 or bracket != pairs[stack.pop()]:
        #         return False
        # return len(stack) == 0

        # Number 2
        # opcl = dict(('()','[]','{}'))
        # stack = []
        # for idx in s: 
        #     if idx in '([{':
        #         stack.append(idx)
        #     elif len(stack) == 0 or idx != opcl[stack.pop()]:
        #         return False
        # return len(stack) == 0

        # Number # 3 
        # d = {'(':')','{':'}','[':']'}
        # stack = []
        # for i in s:
        #     if i in d: 
        #         stack.append(i)
        #     elif len(stack) == 0 or d[stack.pop()] !=i: 
        #         return False
        # return len(Stack) == 0 

        # Number # 4 
        # ack = []
        # lookfor = {')':'(', ']':'[', '}':'{'}

        # for p in s:
        #     if p in lookfor.values():
        #         ack.append(p)
        #     elif ack and lookfor[p] == ack[-1]:
        #         ack.pop()
        #     else:
        #         return False

        # return ack == []

        # Number # 5 
        stk = []
        for ch in s: 
            if not stk: 
                stk.append(ch)
            elif stk[-1] == '(' and ch == ')':
                stk.pop()
            elif stk[-1] == '[' and ch == ']':
                stk.pop()
            elif stk[-1] == '{' and ch == '}':
                stk.pop()
            else:
                stk.append(ch)
        if not stk:
            return True
        return False