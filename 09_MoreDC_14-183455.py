name_c = str(input())
name_t = str(input())
name_d = str(input())

courses = {}
teachers = {}
match = ''

c = open(name_c, 'r')
for i in c:
    n, id = i.split(',')
    courses[int(n)] = int(id)
c.close()

t = open(name_t, 'r')
for j in t:
    m, name = j.split(',')
    teachers[int(m)] = name
t.close()

d = open(name_d, 'r')
for k in d:
    cid, tn = k.split(',')
    if int(cid) not in courses.keys() or int(tn) not in teachers.keys():
        match += 'record error\n'
    else:
        match += str(courses[int(cid)]) + ',' + teachers[int(tn)]
d.close()

print(match)
