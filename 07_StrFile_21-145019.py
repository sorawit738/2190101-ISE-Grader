def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    alpha1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    alpha2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha1upper = [str(i).upper() for i in alpha1]
    alpha2upper = [str(i).upper() for i in alpha2]
    string_list = []
    while True:
        s = str(input())
        if s == 'end':
            break
        string_list += [s]
    
    for i in range(len(string_list)):
        s2 = ''
        string_list2 = []
        string_list2 += string_list[i]
        for j in range(len(string_list2)):
            if string_list2[j] in alpha1:
                string_list2[j] = alpha2[search(alpha1, string_list2[j])]
            elif string_list2[j] in alpha2:
                string_list2[j] = alpha1[search(alpha2, string_list2[j])]
            elif string_list2[j] in alpha1upper:
                string_list2[j] = alpha2upper[search(alpha1upper, string_list2[j])]
            elif string_list2[j] in alpha2upper:
                string_list2[j] = alpha1upper[search(alpha2upper, string_list2[j])]
        for k in string_list2:
            s2 += k
        print(s2)