def array_count9(nums):
    count = 0

    for items in nums:
        if item == 9:
            count = count + 1

    return count 

def first_last6(nums):
    if nums[0]==6 or nums[len(nums) - 1]==6:
        return True
    else:
        return False

def same_first_last(nums):
    if len(nums) == 1 or len(nums) > 1:
        if nums[0] == nums[len(nums) - 1]:   
            return True
     
    return False
  
def make_pi():
    nums = [3,1,4]
    return nums 

def common_end(a, b):
    if len(a) > 0 and len(b) > 0:
        if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
            return True
      
    else:
        return False 
    
def sum3(nums):
    return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
    left = [nums[len(nums)-2], nums[len(nums)-1], nums[0]]
    return left

def reverse3(nums):
    reverse3 = [0,0,0]
    reverse3 [0] = nums[2]  
    reverse3 [1] = nums[1]
    reverse3 [2] = nums[0]
    return reverse3

def max_end3(nums):
    f = nums[0]
    l = nums[2]
    if f > l:
        return [nums[0], nums[0], nums[0]]
    
    else:
        return [nums[2], nums[2], nums[2]]
    
def sum2(nums):
    if len(nums) == 2:
        return nums[0] + nums[1]
    
    if len(nums) > 2:
        return nums[0] + nums[1]
    
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]

def middle_way(a, b):
    return [a[1], b[1]] 

def make_ends(nums):
    return [nums[0], nums[len(nums) - 1]]

def has23(nums):
    if nums[0] == 2 or nums[1] == 2:
        return True
    if nums[0] == 3 or nums[1] == 3:
        return True
        
    else:
        return False 
    
def count_evens(nums):
    count = 0
    for items in nums:
        if (items % 2) == 0:
            count = count + 1
    return count 

def big_diff(nums):
    smallest = nums [0]
    
    for i in range (1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            
    largest = nums[0]
    for i in range (1, len(nums)):
        if nums[i] > largest:
            largest = nums[i]
            
    return largest - smallest    
    
def has22(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 2 and nums[i +1] == 2:
            return True
        
    return False