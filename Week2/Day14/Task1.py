nums = [2,7,11,15]
target = 9
def twoSum(nums, target):
    dict = set()
    for num in nums:
        if num in dict:
            print(f"the targeted number is {num} and {target - num}")
            return num, target - num
        dict.add(target - num)

    print(f"Your two sum is not applicable here")
twoSum(nums, target)