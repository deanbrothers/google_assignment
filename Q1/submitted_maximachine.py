#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

maxi_array = ['P1', 'P2', 'P3', 'M1', 'M2', 'M3']
maxi_value = {'P1':-2, 'P2':-4, 'P3':'w/2', 'M1':2, 'M2':4, 'M3':'w*2'}

def get_work_sum(work):
    """Function will find the sum of work"""
    work_sum = 0
    for w in work:
        if w not in ['P3', 'M3']:
            work_sum = work_sum + maxi_value[w]
        if w == 'P3':
            work_sum = round(work_sum/2)
        if w == 'M3':
            work_sum = work_sum * 2
        if work_sum <= 0 or work_sum > 16:
            work_sum = 0
            break
    return work_sum


def get_combination_set(input_set):
    """Function to find possible combibation set"""
    combination_set = []
    for i, x in enumerate(input_set):
        if x > 0:
            for j in range(x):
                combination_set.append(maxi_array[i])
    return combination_set


def get_max_work(possible_work):
    """Function to find the max work"""
    max_work = 0
    for work in possible_work:
        if work[0] in ['P1', 'P2', 'P3']:
            pass
        else:
            work_sum = get_work_sum(work)
            if work_sum > max_work and work_sum <= 16 and work_sum > 0:
                max_work = work_sum

    return max_work
    


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
    combination_set = get_combination_set(input_set)
    possible_work = permutations(combination_set, total_length)
    max_work_value = get_max_work(possible_work)
    print(max_work_value)

