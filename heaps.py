import heapq

# Given an integer array nums and an integer k, return the kth largest element in the array.
def findKthLargest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  

# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
def trapRainWater(heightMap):
    if not heightMap or not heightMap[0]:
        return 0
    
    m, n = len(heightMap), len(heightMap[0])
    visited = [[False] * n for _ in range(m)]
    min_heap = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heapq.heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    water_trapped = 0
    current_max_height = 0
    
    while min_heap:
        height, x, y = heapq.heappop(min_heap)
        current_max_height = max(current_max_height, height)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if height > heightMap[nx][ny]:
                    water_trapped += height - heightMap[nx][ny]
                heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
    
    return water_trapped
heightMap = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 5],
    [6, 1, 4, 5, 4, 6],
    [5, 1, 1, 2, 1, 5],
    [5, 1, 4, 6, 2, 5]
]
print(trapRainWater(heightMap))

 # Find the Smallest Range Covering Elements from K Lists
def smallestRange(lists):
    min_heap, current_max, range_start, range_end = [], float('-inf'), float('-inf'), float('inf')
    
    for i, lst in enumerate(lists):
        heapq.heappush(min_heap, (lst[0], i, 0))
        current_max = max(current_max, lst[0])
    
    while min_heap:
        current_min, list_index, element_index = heapq.heappop(min_heap)
        if current_max - current_min < range_end - range_start:
            range_start, range_end = current_min, current_max
        
        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, list_index, element_index + 1))
            current_max = max(current_max, next_val)
        else:
            break
    
    return [range_start, range_end]

#Compute the running median of a sequence of numbers.
class MedianFinder:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num):
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, -num) if self.min_heap else -num)
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self):
        return (-self.max_heap[0] + self.min_heap[0]) / 2 if self.max_heap and self.min_heap else -self.max_heap[0]

#You are given an array of k linked lists, each sorted in ascending order. Merge all the linked lists into one sorted linked list and return it.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = [(l.val, l) for l in lists if l]
    heapq.heapify(min_heap)
    dummy = ListNode(0)
    current = dummy
    
    while min_heap:
        val, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, node.next))
    
    return dummy.next