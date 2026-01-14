def binarySearch(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

list1 = [x**2  for x in range(1,15)]
print(list1)
print(binarySearch(list1,25))