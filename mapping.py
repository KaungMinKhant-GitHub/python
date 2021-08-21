nums = [2,1,4,6,5,7]
# map(funciton , nums)
def mapfunc(num):
    return num*2

print(list(map(mapfunc,nums)))

nums = [num * 2 for num in nums]
print(nums)