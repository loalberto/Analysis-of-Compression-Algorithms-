# https://www.geeksforgeeks.org/run-length-encoding-python/ with modifications done by me.
# Author: Shashank Mishra(Gullu)

from collections import OrderedDict
import random
import string
import time


def run_length_encoding(value):
    count = 0
    # Generate ordered dictionary of all lower
    # case alphabets, its output will be
    # dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0}
    dictionary = OrderedDict.fromkeys(value, 0)

    # Now iterate through input string to calculate
    # frequency of each character, its output will be
    # dict = {'w':4,'a':3,'d':1,'e':1,'x':6}
    for ch in value:
        count += 1
        dictionary[ch] += 1

    # now iterate through dictionary to make
    # output string from (key,value) pairs
    output = ''
    for key in dictionary:
        output = output + key + str(dictionary[key]) + '#'
    return output, count


# used to generate a random string
def random_string(string_length):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


# Driver function
if __name__ == "__main__":

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

    itr = 10
    while itr != 0:
        n = 10
        while n <= 100000:
            start_time = time.time()
            val = random_string(n)
            end_time = time.time()
            total_time = (end_time - start_time) * 1000000000
            output = run_length_encoding(val)

            op_matrix[y].append(output[1])
            time_matrix[b].append(total_time)
            n *= 10
        x += 1
        a += 1
        y = 'Iteration{}'.format(x)
        b = 'Iteration{}'.format(a)
        itr -= 1

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