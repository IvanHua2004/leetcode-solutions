class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [1] + [0] * k
        for N in range(1, n + 1):
            for j in range(min(N, k), 0, -1):
                dp[j] = (dp[j-1] + (N-1) * dp[j]) % MOD
            dp[0] = 0
        return dp[k]