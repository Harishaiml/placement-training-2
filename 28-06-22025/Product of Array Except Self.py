def productExceptSelf(nums):
    length = len(nums)
    answer = [1] * length

    left = 1
    for i in range(length):
        answer[i] = left
        left *= nums[i]

    right = 1
    for i in reversed(range(length)):
        answer[i] *= right
        right *= nums[i]

    return answer
