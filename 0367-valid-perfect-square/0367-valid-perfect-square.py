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
        length = num//2
        if num > 2**15:
            length = (num//150)
        
        for i in range(2, length+1):
            if i*i == num:
                return True
            if i*i > num:
                return False
        return False