import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        heapq.heapify(self.nums)
        while len(self.nums)>k:
            # pop the smallest elements, until we have the k largest elements left
            # in this min heap, the head of the heap will now contain the k-th largest element (i.e. the smallest one among the k largest elements left in the heap)
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # check if the length of the input array is > than k
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
