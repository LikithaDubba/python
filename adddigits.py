class Solution:
    def addDigits(self,num:int)->int:
        if num==0:
            return 0
        return 1+(num-1)%9
    
class solution:
    def addDigits(self,num:int)->int:
        while num>9:
            t=0
            while num>0:
                t+=num%10
            num//=10
        return num