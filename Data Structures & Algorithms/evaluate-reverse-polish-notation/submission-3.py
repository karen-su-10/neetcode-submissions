class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calStack =[]
        operators ={"+", "-","*",'/'}
        #edge case 
        if len(tokens)==1:
            return int(tokens[0])
        for t in tokens:
            if t not in operators:
                calStack.append(t)
            else:
                a = int(calStack.pop())
                b = int(calStack.pop())
                if t == "+":
                    r = a + b
                    calStack.append(r)
                if t == "-":
                    r = b - a
                    calStack.append(r)
                if t == "*":
                    r = a * b
                    calStack.append(r)
                if t == "/":
                    r = int(b / a)
                    calStack.append(r)
        return calStack[0]