#Solution

def bitmanipulation(nums,i):
    bit = i-1

    get_bit = (nums >> bit) & 1
    set_bit = nums | (1 << bit)
    clear_bit = nums & ~(1 << bit)

    print(get_bit,set_bit,clear_bit)

