class MedianFinder:
    def __init__(self):
        self.small, self.large = [], [] # two heaps, heaps should be equal size


    def addNum(self, num):
        heapq.heappush(self.small, -1 * num)
        # python doesn't have a max heap
        # so we multiply by -1 to implement it

        # every num in small <= large
        # if not, pop and push to large
        if (self.small and self.large and
                (-1 * self.small[0] > self.large[0])):
                # if the largest value in the small heap is larger than the the smallest value in the small heap
                # pop the value and add it to the large heap, because small heap <= large heap always

        val = -1 * heapq.heappop(self.small)
        heapq.heappush(self.large, val)


        # uneven size

        if (len(small) > len(large) + 1):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if (len(large) > len(small) + 1):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self):
        if len(small) > len(large):
            return -1 * self.small[0]
        if len(large) > len(small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2
