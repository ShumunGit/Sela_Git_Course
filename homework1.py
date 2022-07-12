# A.
lst = [3,7,2]
histo = []

for i in lst:
    histo.append("*"*i)
print(histo)

# B.
lst1=["a","b","c"]
lst2 = ["x","y","z"]
lst_res=[]
lst2Len = len(lst2)-1
for i in range(len(lst1)):
    neWord = lst1[i]+lst2[lst2Len]
    lst_res.append(neWord)
    lst2Len -= 1
print(lst_res)

# C.
lstOflst = [1,2,3,[4,5,[6]],5,[4,3,8],90,50,[22,33,44,55]]
newLst = []
for num in lstOflst:
    if type(num) == type([]):
        newLst.extend(num)
    else:
        newLst.append(num)
print(newLst)
