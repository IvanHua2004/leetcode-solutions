class Solution:
    def specialPerm(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        full = (1 << n) - 1
        ok = [[a % b == 0 or b % a == 0 for b in nums] for a in nums]
        memo = {}

        def dfs(mask, last):
            if mask == full:
                return 1
            if (mask, last) in memo:
                return memo[(mask, last)]

            total = 0
            for next in range(n):
                if not mask >> next & 1 and ok[last][next]:
                    total += dfs(mask | 1 << next, next)

            memo[(mask, last)] = total % MOD
            return memo[(mask, last)]

        ans = 0
        for i in range(n):
            ans += dfs(1 << i, i)
        return ans % MOD