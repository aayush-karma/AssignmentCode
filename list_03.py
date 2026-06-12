#3 append method
l=[12,13,14,15,16,17,18,20]
l.append(45)
print("append 45",l)

#4 insert method
l.insert(9,55)
print("insert 55",l)

#5 remove list item
l.remove(45)
print("remove  45",l)

#6 Clear entrie list
l.clear()
print("clear whole list",l)

newlst=[10,20,30,40,50,60,70,80,90]
#7 length of list
print("length",len(newlst))

#8 sum of list
total=0
for a in newlst:
    total=total+a
    print(total)

#9 interchange 1st and last number
x =newlst[0] 
newlst[0]=newlst[-1]
newlst[-1]=x
print(newlst)

#10     

#12 reverse the list
newlst.reverse()
print(newlst)

