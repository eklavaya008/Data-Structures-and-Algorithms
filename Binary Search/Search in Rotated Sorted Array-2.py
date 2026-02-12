#Solution

def rotate_arr1(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]:
            high-=1
            low+=1
            continue
        if nums[low]<=nums[mid]:
            if nums[low]<=target<=nums[mid]:
                high = mid -1
            else:   
                low = mid +1
        else:
            if nums[mid]<=target<=nums[high]:
                low = mid +1
            else:
                high = mid-1
    return False


nums = [2,5,6,0,0,1,2]
target = 0
print(rotate_arr1(nums,target))
