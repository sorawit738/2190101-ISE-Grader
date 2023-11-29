import numpy as np

def sum_2_rows(M):
    return M[::2] + M[1::2]

def sum_left_right(M):
    columns = M.shape[1]
    return M[:, int(columns / 2):] + M[:, :int(columns / 2)]

def sum_upper_lower(M):
    rows = M.shape[0]
    return M[int(rows / 2):, :] + M[:int(rows / 2), :]

def sum_4_quadrants(M):
    rows = M.shape[0]
    columns = M.shape[1]
    return M[:int(rows / 2), :int(columns / 2)] + M[:int(rows / 2), int(columns / 2):] + M[int(rows / 2):, :int(columns / 2)] + M[int(rows / 2):, int(columns / 2):]

def sum_4_cells(M):
    return M[0::2, 0::2] + M[1::2, 0::2] + M[0::2, 1::2] + M[1::2, 1::2]

def count_leap_years(years):
    results = []
    for e in years:
        if (e - 543) % 400 == 0 or ((e - 543) % 4 == 0 and ((e - 543) % 100 != 0)):
            results.append(e)
    return len(results)

exec(input().strip())
