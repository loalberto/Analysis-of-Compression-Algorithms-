# https://rosettacode.org/wiki/LZW_compression#Python

import string
import random
import time

def compress(uncompressed):
    """Compress a string to a list of output symbols."""
    count = 0
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        count += 1
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result, count

def random_string(string_length):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


# How to use:
# compressed = compress(random_string(10))
# print(compressed)

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
        start_time = time.time()
        comp = compress(random_string(n))
        end_time = time.time()
        total_time = (end_time - start_time) * 1000000000

        op_matrix[y].append(comp[1])
        time_matrix[b].append(total_time)
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
