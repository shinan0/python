students = {}
f = open('C:/Users/12428/Desktop/students.txt','r'，encoding='utf-8')
lines=f.readlines()
for line in lines:
    tmp1=line.split(',')
    #print(tmp1)
    xuehao = tmp1[0]
    xingming = tmp1[1]
    students[xuehao] = xingming
f.close()
import random
num = eval(input(''))
results=random.sample(students.keys(),num)
for xuehao in results:
    print(students[xuehao]