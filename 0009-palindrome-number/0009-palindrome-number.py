class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        if temp < 0:
            return False
        elif temp == 0:
            return True
        listt = []
        while temp > 0:
            r = temp % 10
            temp = temp // 10
            listt.append(r)
        i = 0
        j = len(listt) - 1
        while (i < j):
            if(listt[i] != listt[j]):
                return False
            else:
                i += 1
                j -= 1
        return True