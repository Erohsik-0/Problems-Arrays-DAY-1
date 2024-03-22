class Solution:
    def reArrange(self , l):
        return sorted(l)

if __name__ == "__main__":
    l = list(map(int , input().split(", ")))
    l = Solution().reArrange(l)
    print(*l)