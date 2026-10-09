class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2!=0:
            return False
        bracketMap ={"(":")", "[":"]", "{":"}"}
        stack = []
        for i in s:
            # put in stack if left bracket
            if i in bracketMap:
                stack.append(i)
            #else: should be right bracket, then pop the previous from the stack, validate
            else:
                if not bool(stack):
                    return False
                memo = stack.pop()
                pair=bracketMap.get(memo)
                if pair!=i:
                    return False
        #at the end , the stack should be empty afte poping out all elements
        if  bool(stack):
            return False
        return True
                
   

        