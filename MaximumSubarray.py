class Solution:
    def maxSubArray(self, nums):
        # Step 1: Start with first element as initial values
        currentSum = nums[0]   # Best sum ending at current position
        maxSum = nums[0]       # Best sum found so far

        # Step 2: Traverse from second element onwards
        for i in range(1, len(nums)):
            # Either:
            # 1) Start new subarray from nums[i]
            # 2) Or, extend the previous subarray by adding nums[i]
            currentSum = max(nums[i], currentSum + nums[i])

            # Update global maximum if needed
            maxSum = max(maxSum, currentSum)

        # Step 3: Final answer
        return maxSum
