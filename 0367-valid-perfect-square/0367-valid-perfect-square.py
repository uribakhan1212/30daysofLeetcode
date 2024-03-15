class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num > (2**31)-1:
            return False
        
        root = int(num**0.5)
        
        return root*root == num