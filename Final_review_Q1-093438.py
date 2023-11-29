import numpy as np

def get_consensus(ss):
    # write your code here.
    possible_char = 'ACGT'
    consensus = ''
    s = ss.upper().split('\n')
    m = np.zeros((len(possible_char), len(s[0])), dtype=int)
    for e in s:
        for i in range(len(e)):
            ro = possible_char.find(e[i])
            co = i
            m[ro, co] += 1
    ma = np.max(m, axis=0)
    for j in range(len(s[0])):
        temp = ''
        for e2 in np.where(m[:, j] == ma[j])[0]:
            if len(temp) == 0:
                temp += possible_char[e2]
            else:
                temp += '/' + possible_char[e2]
        consensus += temp
        if j < len(s[0]) - 1:
            consensus += ' '
    return consensus # DO NOT MODIFY THIS LINE

def get_consensus_generic(ss):
    # write your code here.
    possible_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    consensus = ''
    s = ss.upper().split('\n')
    n = len(s[s.index(max(s, key=len))])
    m = np.zeros((len(possible_char), n), dtype=int)
    for e in s:
        for i in range(len(e)):
            ro = possible_char.find(e[i])
            co = i
            m[ro, co] += 1
    ma = np.max(m, axis=0)
    for j in range(n):
        temp = ''
        for e2 in np.where(m[:, j] == ma[j])[0]:
            if len(temp) == 0:
                temp += possible_char[e2]
            else:
                temp += '/' + possible_char[e2]
        consensus += temp
        if j < n - 1:
            consensus += ' '
    return consensus # DO NOT MODIFY THIS LINE

exec(input().strip())
