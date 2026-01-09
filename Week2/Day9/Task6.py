def square(nums):
    for num in nums:
        yield num**2

def filter(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

nums = [1,2,3,4,5,6,7,8,9,10]
for value in filter(square(nums)):
    print(value)