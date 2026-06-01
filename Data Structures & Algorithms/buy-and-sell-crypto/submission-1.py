class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      left = 0 
      right = 1 
      n = len(prices)
      max_profit = 0 
      while right<n:
        if prices[right]<prices[left]:
            
            left = left+1 
        
        else: 

            x = prices[right]-prices[left]
            if x>max_profit:
                max_profit = x 

            right=right+1
                

    
      return max_profit

     
