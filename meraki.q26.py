# fruit = {}
# def addone(index):
#     if index  in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone("apple")
# addone("apple")
# addone("banana")
# addone("apple")
# print(fruit)
# print(len(fruit))


# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(len(Details)) 




# print [1,"p",2,"o",3,"o",4,"j",5,"a"]
# a=[1,2,3,4,5]
# b="pooja"
# s=[]
# i=0
# while i<len(a):
#     s.append(b[i])
#     s.append(a[i])
#     i=i+1
# print(s)




my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
s=0
for i in my_dict:
    s+=my_dict[i]
print(s)
print(my_dict)


