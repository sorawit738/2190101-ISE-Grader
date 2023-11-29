# function1

def find_index(a, t):
    for i in range(len(a)):
        if a[i] == t:
            return i
    return -1

def create_record():
    # get input from keyboard: messy travel records
    # return: records - a list of lists of records
    records = []
    x = str(input())
    while x != 'q':
        records += [x.split()]
        x = str(input())
    return records

# function2
def sort_list(records):
    # input: a list of lists of record
    # return: sorted_records - sorted version of the input
    #names = [e[0] for e in records]
    #dates = [e[1].split('/') for e in records]
    #country = [e[2] for e in records]
    for i in range(len(records)):
        position = i
        d1, m1, y1 = records[position][1].split('/')
        for j in range((position + 1), len(records)):
            d2, m2, y2 = records[j][1].split('/')
            if records[j][0] < records[position][0]:
                position = j
            elif records[j][0] == records[position][0] and int(y2) < int(y1):
                position = j
            elif records[j][0] == records[position][0] and int(y2) == int(y1) and int(m2) < int(m1):
                position = j
            elif records[j][0] == records[position][0] and int(y2) == int(y1) and int(m2) == int(m1) and int(d2) < int(d1):
                position = j
        records[i], records[position] = records[position], records[i]
    return records

# function3
def create_output(sorted_records):
    # input: sorted records
    # return: (1) a list of user’s name and (2) a list of trip’s details with the index of each list corresponding to one another
    result = []
    names = []
    dates = []
    for e in sorted_records:
        if e[0] not in names:
            names += [e[0]]
            dates += [[e[1] + ':' + e[2]]]
        else:
            dates[find_index(names, e[0])].append(e[1] + ':' + e[2])

    result += [names]
    result += [dates]
    return result

# the main function
def main():
    # call these three methods
    # print out the sorted output in the correct format back to the user
    r = create_record()
    sorted_r = create_output(sort_list(r))
    if len(r) == 0:
        print('No records!')
    else:
        for e in range(len(sorted_r[0])):
            print(sorted_r[0][e], sorted_r[1][e])

exec(input())
