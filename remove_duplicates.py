def remove_duplicates(list):
    for ele in list:
        count=0
        temp=ele
        for j,i in enumerate(list):
            if temp==i:
                count+=1
                if count>1:
                    del list[j]
    return list
list=[1,2,3,3,4,5,55,1,3,4,6,4]
print(remove_duplicates(list))