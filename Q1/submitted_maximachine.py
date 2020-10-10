#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

machine_line = ['P1', 'P2', 'P3', 'M1', 'M2', 'M3']
work_value = {'P1':-2, 'P2':-4, 'P3':'w/2', 'M1':2, 'M2':4, 'M3':'w*2'}

def get_work(work):
    sum = 0
    for w in work:
        if w not in ['P3', 'M3']:
            sum = sum + work_value[w]
        if w == 'P3':
            sum = round(sum/2)
        if w == 'M3':
            sum = sum * 2
        if sum <= 0 or sum > 16:
            sum = 0
            break
    return sum


def get_assembly(input_set):
    assembly_set = []
    for i, x in enumerate(input_set):
        if x > 0:
            for j in range(x):
                assembly_set.append(machine_line[i])
    return assembly_set



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    p1 = int(first_multiple_input[0])

    p2 = int(first_multiple_input[1])

    p3 = int(first_multiple_input[2])

    m1 = int(first_multiple_input[3])

    m2 = int(first_multiple_input[4])

    m3 = int(first_multiple_input[5])
    input_set = [int(inp) for inp in first_multiple_input]
    total_length = sum(input_set)
    assembly_line = get_assembly(input_set)
    possible_work = permutations(assembly_line, total_length)
    max_work = 0
    for work in possible_work:
        if work[0] in ['P1', 'P2', 'P3']:
            pass
        else:
            work_sum = get_work(work)
            if work_sum > max_work and work_sum <= 16 and work_sum > 0:
                max_work = work_sum

    print(max_work)

