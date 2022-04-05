def solution(nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= 5:
            l = mid + 1
        else:
            r = mid - 1

    return l

nums = [1,2,3,4,4,5,5,5,5,8,9]
a = solution(nums)
print(a)