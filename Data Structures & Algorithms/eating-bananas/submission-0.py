class Solution:
    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # fine the largest pile and the max rate = height of that pile to get total hr = target 
        # then cut in half, check if total hr <= target h, move left /right
        upperbound_rate = max(piles)
        lowerbound_rate = 1
        def get_actual_hr(curr_rate, piles):
            total_hr = 0
            for item in piles:
                if item <=curr_rate:
                    total_hr +=1
                else:
                    # curr_hr = item//curr_rate
                    curr_hr = (item + curr_rate - 1) // curr_rate
                    total_hr = total_hr + curr_hr
            return total_hr

        while lowerbound_rate <= upperbound_rate:
            curr_rate= lowerbound_rate + (upperbound_rate-lowerbound_rate)//2
        # use current rate to get a hr, if hr>=target h, reset left_rate/right_rate, rate_pr
            total_hr = get_actual_hr(curr_rate, piles)
            if total_hr > h:
                #rate increase
                #lowerbound_rate = curr_rate -- repeated mid point
                lowerbound_rate = curr_rate +1
            else:
                 #rate decrease
                 upperbound_rate = curr_rate -1
        # not curr_rate, but lowerbound_rate
        return lowerbound_rate
    
    
            
        