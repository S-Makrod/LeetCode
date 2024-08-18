from functools import reduce
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = reduce(lambda x, y: x if y == 0 else x * y, nums)
        # zero_count = nums.count(0)

        # if zero_count > 1:
        #     return [0 for num in nums]

        # sol = []

        # for num in nums:
        #     if zero_count > 0 and num != 0:
        #         sol.append(0)
        #     elif zero_count > 0 and num == 0:
        #         sol.append(prod)
        #     else:
        #         sol.append(prod//num)

        # return sol

        pre = []
        post = []

        for i in range(len(nums)):
            if i == 0:
                pre.append(1)
            else:
                pre.append(pre[i - 1] * nums[i - 1])

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post.append(1)
            else:
                post = [post[0] * nums[i + 1]] + post

        return [pre[i] * post[i] for i in range(len(nums))]
