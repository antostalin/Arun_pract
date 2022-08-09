# The program to sum of n numbers and find which is the best way to implement this
# How to define the solution will be good compared to other
import timeit

def sum(n):
    final_sum = 0
    for x in range(n + 1):
        final_sum += x
    return final_sum


def sumalg(n):
    return (n * (n + 1)) / 2


def sum_time():
    SETUP_CODE = '''from __main__ import sum'''
    SUM_CODE = '''sum(100)'''
    timer = timeit.repeat(setup=SETUP_CODE, stmt=SUM_CODE, repeat=3, number=10000)
    print("Iterative Sum time: {}".format(min(timer)))


def sumalg_time():
    SETUP_CODE = '''from __main__ import sumalg'''
    SUM_ALG_CODE = '''sumalg(100)'''
    timer = timeit.repeat(setup=SETUP_CODE, stmt=SUM_ALG_CODE, repeat=3, number=10000)
    print("Algorithm Sum time: {}".format(min(timer)))


if __name__ == '__main__':
    # time and space complexity of the program
    # timeit.timeit(setup, stmt, timer, repeat, number)
    sum_time()
    sumalg_time()
