from typing import List
class Solution:
    def compare(self , x: str, y: str) -> int:
        xy = x + y
        yx = y + x
        if xy > yx:
            return -1
        elif xy < yx:
            return 1
        else:
            return 0

    def printLargest(self , arr : List[int]) -> str:
        arr_str = [str(x) for x in arr]
        arr_str.sort(key=lambda x: self.compare(x, x))
        result = ''.join(arr_str)
        return result

if __name__ == "__main__":
    l = list(map(int , input().split(", ")))
    print(Solution().printLargest(l))