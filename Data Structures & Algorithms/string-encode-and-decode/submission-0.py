class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
          encoded_str=encoded_str+str(len(i))+'#'+i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list =[]
        #go through each char using pointer technique
        p = 0
        while p <len(s):
            q = s.find('#', p)
            length = int(s[p:q])
            word = s[q+1:q+1+length]
            decoded_list.append(word)
            p = q+1+length
        return decoded_list
            
            


        
            
