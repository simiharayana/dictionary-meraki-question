# # Write a program remove the first key value pair from a nested dictionary.

Dic=  {1: 'NAVGURUKUL',2: 'IN',  3:{ 'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del(Dic[3]['A'])
# print(Dic)
d={}
for i in Dic:
    if type(Dic[i])==dict:
        # print(Dic)
        d1={}
        for y in Dic[i]:
            # a={}
            if y!="A":
                d1.update({y:Dic[i][y]})
        d.update({i:d1})        
    else:
        d.update({i:Dic[i]})
print(d)
                
