lst1=[]
lst2=[]

while True:
    s=str(input())
    if s=='END':
        break
    else:
        lst1.append(s)
        
for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i][:4]==lst1[j][:4]:
            if len(lst1[i])>len(lst1[j]):
                lst1[j]=lst1[i]
            else:
                lst1[i]=lst1[j]
s=str(input())
for i in range(0,len(lst1),2):
    if s in lst1[i] or lst1[i] in lst2:
        lst2.append(lst1[i+1])
lst2=sorted(lst2, key=lambda x: int(x[:4]))
for i in range(len(lst2)):
    if len(lst2[i])<6:
        print(lst2[i]+"Unknown Name")
    else:
        print(lst2[i])
