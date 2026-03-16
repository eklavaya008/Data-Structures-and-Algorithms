#Solution

def countSetBits(self,n):
        total = 0
        while n>0:
            x = n.bit_length() - 1
            p = 1<<x
            total += x * (p >> 1)
            total += n - p + 1
            n = n - p
        return total
