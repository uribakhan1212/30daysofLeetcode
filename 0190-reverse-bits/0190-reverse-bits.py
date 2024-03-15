class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        n = bin(int(n))
        n = int(n, 2)
        n = format(n, 'b')
        n = n.zfill(32)
        return int(n[-1::-1], 2)
        
        