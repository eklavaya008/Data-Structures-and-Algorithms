#Solution

def check_ithbit(nums,k):
    if ((nums>>k) & 1) != 0:
        return True
    else:
        return False