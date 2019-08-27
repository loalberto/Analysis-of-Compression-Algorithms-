# https://rosettacode.org/wiki/Huffman_coding#Python
# Author: Rosetta Code

from heapq import heappush, heappop, heapify
from collections import defaultdict
import string
import random
import time


def encode(values):
    count = 0
    heap = []
    """Huffman encode the given dict mapping symbols to weights"""
    #
    for sym, wt in values.items():
        # print(wt)
        count += 1
        heap.append([wt, [sym, ""]])
    heapify(heap)
    while len(heap) > 1:
        count += 1
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda val: (len(val[-1]), val)), count


def random_string(string_length):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


itr = 10
op_matrix = {'Iteration1': [],
             'Iteration2': [],
             'Iteration3': [],
             'Iteration4': [],
             'Iteration5': [],
             'Iteration6': [],
             'Iteration7': [],
             'Iteration8': [],
             'Iteration9': [],
             'Iteration10': []}

time_matrix = {'Iteration1': [],
               'Iteration2': [],
               'Iteration3': [],
               'Iteration4': [],
               'Iteration5': [],
               'Iteration6': [],
               'Iteration7': [],
               'Iteration8': [],
               'Iteration9': [],
               'Iteration10': []}

x = 1
y = 'Iteration{}'.format(x)
a = 1
b = 'Iteration{}'.format(a)
while itr != 0:
    itr -= 1
    n = 10
    while n <= 100000:
        txt = random_string(n)
        huffman = defaultdict(int)
        first_count = 0

        for ch in txt:
            first_count += 1
            huffman[ch] += 1

        start_time = time.time()
        vals = encode(huffman)
        end_time = time.time()
        total_time = (end_time - start_time) * 1000000000

        total = vals[1] + first_count
        op_matrix[y].append(total)
        time_matrix[b].append(total_time)
        # print("Symbol\tWeight\tHuffman Code")
        # for p in vals[0]:
        #     print("{} \t\t {} \t\t\t {}".format(p[0], huffman[p[0]], p[1]))
        n *= 10
    x += 1
    y = 'Iteration{}'.format(x)
    a += 1
    b = 'Iteration{}'.format(a)

res = {}

for i in range(0, len(op_matrix['Iteration1'])):
    res[i] = 0

for key in op_matrix:
    x = 0
    for i in op_matrix[key]:
        res[x] += i
        x += 1

for key in res:
    val = res[key]
    res[key] = val / 10

op_matrix['Average'] = []

for key in res:
    op_matrix['Average'].append(res[key])

res = {}

for i in range(0, len(time_matrix['Iteration1'])):
    res[i] = 0

for key in time_matrix:
    x = 0
    for i in time_matrix[key]:
        res[x] += i
        x += 1

for key in res:
    val = res[key]
    res[key] = val / 10

time_matrix['Average'] = []

for key in res:
    time_matrix['Average'].append(res[key])

print('\n\n------------This is for the operation measurement------------\n\n')


for key in op_matrix:
    print(key + ' ' + str(op_matrix[key]))

print('\n\n------------This is for the time measurement------------\n\n')


for key in time_matrix:
    print(key + ' ' + str(time_matrix[key]))
