from collections import defaultdict
class Solution:
    def subarraySum(self , nums, k):
        count = 0
        prefix_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        
        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k
            if complement in sum_freq:
                count += sum_freq[complement]
            sum_freq[prefix_sum] += 1
        
        return count


if __name__ == "__main__":
    l = list(map(int , input().split(",")))
    k = int(input())
    print(Solution().subarraySum(l , k))