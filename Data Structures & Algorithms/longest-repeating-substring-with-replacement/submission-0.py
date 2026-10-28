class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        left = 0
        max_length = 0

        for right in range(len(s)):

            # 1. Expand：更新新字符的频率
    
            right_value = s[right]
            frequency[right_value] = frequency.get(right_value, 0)+1


            # 2. 计算当前窗口的 max_frequency
      
            max_frequency = max(frequency.values())

            
            # 3. Shrink：恢复窗口合法性
            while (right - left +1 )-max_frequency > k:

                # 更新移出字符的频率
                left_value = s[left]
                frequency[left_value] -=1

                # 移动 left
                left = left +1

                # 重新计算 max_frequency
                max_frequency = max(frequency.values())


            # 4. 更新答案
            max_length = max(max_length,right - left +1)

        return max_length