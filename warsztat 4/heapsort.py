from heapq import heappop, heappush

def heapsort(bbb):
    h = []
    for element in bbb:
        heappush(h, element)

    ordered = []

    
    while h:
        ordered.append(heappop(h))

    return ordered

bbb = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heapsort(bbb))
