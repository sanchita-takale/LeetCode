class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i=0

        # for num in nums:
        #     if i<1 or num > nums[i-1]:
        #         nums[i] = num
        #         i+=1
        # return i
        k = sorted(set(nums))
        for num in range (len(k)):
            nums[num]=k[num]
        # del nums[num+1:]
        print(nums)
        return (len(k))
        # unique_nums = sorted(set(nums))

        # # Copy back into nums (in-place modification)
        # for i in range(len(unique_nums)):
        #     nums[i] = unique_nums[i]

        # # Return the number of unique elements
        # return len(unique_nums)
        