class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num > (2**31)-1 or num < 1:
            return False
        if num > 2**15:
            length = (num//150)
        else:
            length = num//2
  
        
        for i in range(num//length, length+1):
            if i*i == num:
                return True
            if i*i > num:
                return False
        return False