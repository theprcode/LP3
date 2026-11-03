# Aim: To write a Python program to implement Huffman Encoding
# using a greedy strategy.

import heapq

def huffman_encoding(frequencies):
    heap = [[freq, [[char, ""]]] for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for item in left[1]:
            item[1] = "0" + item[1]

        for item in right[1]:
            item[1] = "1" + item[1]

        heapq.heappush(heap, [left[0] + right[0], left[1] + right[1]])

    return sorted(heap[0][1])

frequencies = {
    "A": 5, "B": 9, "C": 12,
    "D": 13, "E": 16, "F": 45
}

codes = huffman_encoding(frequencies)

print("Character  Huffman Code")
for char, code in codes:
    print(char, "        ", code)

# Time Complexity: O(n log n)
# Space Complexity: O(n)
