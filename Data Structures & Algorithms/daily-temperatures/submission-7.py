class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            j = i + 1

            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1

            if j == n:
                res.append(0)
            else:
                res.append(j - i)

        return res