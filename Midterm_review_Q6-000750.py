def mergeRange(ranges):
    ranges.sort()
    result = []
    result.append(ranges[0])
    for e in ranges[1:]:
        if result[-1][0] <= e[0] <= result[-1][-1]:
            result[-1][-1] = max(result[-1][-1], e[-1])
        else:
            result.append(e)

    return result

def remove_patterns(strings): # Task 4.1
    # strings is in the format:
    # original_string,pattern_1,pattern_2,….
    # Find ALL patterns within the original_string and remove them out. If
    # the same pattern found more than once, remove all of them.
    # All remaining fragmented substrings need to be concatenated together
    # in order and return as a new string called edited_string (See
    # Figure 4.1 to see how this function works)
    # Write your code here
    strings_list = strings.split(',')

    s = [c for c in strings_list[0]]

    for i in range(1, len(strings_list)):
        j = len(s)
        while j >= len(strings_list[i]):
            temp = ''.join(s[(j - len(strings_list[i])):j])
            if temp == strings_list[i]:
                del s[(j - len(strings_list[i])):j]
            j -= 1

    edited_string = ''.join(s)

    return edited_string

def check_coverage(strings):  # Task 4.2
    # strings is in the format:
    # reference_string,pattern_1,pattern_2, ….
    # Check if patterns when aligned to the reference string will cover all
    # characters within the reference string.
    # Return string “Covered” if they can cover, otherwise return the
    # indices of all positions in the references that are not covered
    # (See Figure 4.2 to see how this function works
    # Hint: You can use find()
    strings_list = strings.split(',')
    expected = []
    expected.append([0, len(strings_list[0])])
    covered_range = []

    for i in range(1, len(strings_list)):
        temp = [c for c in strings_list[0]]
        while strings_list[i] in ''.join(temp):
            pos = ''.join(temp).find(strings_list[i])
            covered_range.append([pos, pos + len(strings_list[i])])
            for k in range(len(strings_list[i])):
                temp.insert(pos + len(strings_list[i]), '-')
            del temp[pos:(pos + len(strings_list[i]))]

    covered_range = mergeRange(covered_range)
    if covered_range == expected:
       return 'Covered'
    uncovered_range = []
    
    if len(covered_range) == 1:
       if covered_range[0][1] == expected[0][1]:
            uncovered_range.append([(expected[0][1] - 1), (expected[0][1] - 1)])
       elif covered_range[0][1] < expected[0][1]:
            uncovered_range.append([(covered_range[0][1]), (expected[0][1] - 1)])
    for j in range(1, len(covered_range)):
       if j == len(covered_range) - 1 and covered_range[j][1] < expected[0][1]:
            uncovered_range.append([(covered_range[j - 1][1]), (covered_range[j][0] - 1)])
            uncovered_range.append([(expected[0][1] - 1), (expected[0][1] - 1)])
       else:
            uncovered_range.append([(covered_range[j - 1][1]), (covered_range[j][0] - 1)])
    ans = ''
    for k in range(len(uncovered_range)):
       if k == 0:
            ans += str(uncovered_range[k][0]) + '-' + str(uncovered_range[k][1])
       else:
            ans += ',' + str(uncovered_range[k][0]) + '-' + str(uncovered_range[k][1])
    return ans

# Do not remove the following statement
exec(input().strip())
