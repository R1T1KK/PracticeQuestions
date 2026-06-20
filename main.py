# Simple for loops
lists = [1,3,4,5,8,0,6,3,4,6]
for i in lists:
  print(i,end=" ")
print()

for i in range(1,10,2):
  print(i,end=" ")

# Subtract Product Sum
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum_ = 0
        product = 1

        while temp>0:
            r = temp%10
            temp//=10
            sum_+=r
            product *=r
        
        return product - sum_
            
        
        
