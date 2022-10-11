test_list=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# ['2', '7', '9', '5', '1']

i=0
b=[]
while i<len(test_list):
    for j in (test_list[i]):
        if test_list[i][j] not in b:
            b.append(test_list[i][j])
    i+=1
print(b)
