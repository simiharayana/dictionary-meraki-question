# a={"brand":"maruti","modal":"ozire","year":2018}
# print(type(a))
# print(len(a))

###get####

# a={"brand":"maruti","modal":"ozire","year":2018}
# # print(a["brand"])
# d=a.get("modal")
# print(d)

# ##loop through dictionary###
# a={"brand":"maruti","modal":"ozire","year":2018}
# for i in a:
#     print(i)


# a={"brand":"maruti","modal":"ozire","year":2018}
# for i in a:
#     print(a[i])

# #########item funcation##
# a={"brand":"maruti","modal":"ozire","year":2018}
# for x,y in a.items():
    # print(x,y)


###change###
# a={"brand":"maruti","modal":"ozire","year":2018}
# a["modal"]="zomato"
# print(a)



###removing##
# a={"brand":"maruti","modal":"ozire","year":2018}
# a.pop("modal")
# print(a)

# a={"brand":"maruti","modal":"ozire","year":2018}
# b=a.pop("modal")
# print(b)

####popitem:remove the last
# a={"brand":"maruti","modal":"ozire","year":2018}
# a.popitem()
# print(a)

#whene store in variable
# a={"brand":"maruti","modal":"ozire","year":2018}
# dic=a.popitem()
# print(dic)



####del(keyword):delremove t eitem with specified key name

# dic={"brand":"maruti","modal":"ozire","year":2018}
# del dic["model"]
# print(dic)


###clear():dlt all items
# dict={"brand":"maruti","modal":"ozire","year":2018}
# a=dict.clear()
# print(a)


# dict={"brand":"maruti","modal":"ozire","year":2018}
# dict.clear()
# print(dict)



###copy ():copy a dict
# dict={"brand":"maruti","modal":"ozire","year":2018}
# b=dict.copy()
# print(b)

##other way for copy
# a=dict
# print(a)


###fromkeys():return the value with specified key:(if)
# dic={1:"simi",2:"riti",3:"pooja",4:"pinki",5:"samiksha"}
# a="pooja meena"
# b=dic.fromkeys(dic,a)
# print(b)
# a="3.5"
# print(int(float(a)))

###setdefault##3
# dic={1:"simi",2:"riti",3:"pooja",4:"pinki",5:"samiksha"}
# dic.setdefault(8,"fio")
# print(dic)

# a=[2,6,8,9,87,4,]   
# dic.popitem()   
# print(dic)
