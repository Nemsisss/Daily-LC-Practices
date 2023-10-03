class Solution:

    def kthFactor(self, n: int, k: int) -> int:
        # factors = []
        # i = 1
        # while i * i <= n:
        #     if n % i == 0:
        #         factors.append(i)
        #         if n // i != i:
        #             factors.append(n // i)
        #     i += 1
        factors = [i for i in range(1, n + 1) if n % i == 0]
        if len(factors)>0 and len(factors)>=k :
            return factors[k-1]
        return -1
