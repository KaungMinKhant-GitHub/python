nums = [1,2,3,4,5,6,7]
# filter(function , list)
def filer_func(num):
    return (num % 2 == 0)

print(list(filter(filer_func ,nums)))

evennum = []
for num in nums:
    if num % 2 == 0 :
        evennum.append(num)
print(evennum)

nums = [num for num in nums if num % 2 == 0]
print(nums)