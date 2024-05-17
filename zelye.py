otvet=""
n=int(input())
lst=[]
lst2=[]
ten=[]
for i in range(n+1):
    ten.append(str(i))
s="|"
for i in range(n):
    lst.append(str(input()))
s+="f"
s="g"+s
for i in range(len(lst)):
    if lst[i][:3]=="MIX":
        s="MX "+lst[i][4:]+" XM"
    elif lst[i][:4]=="DUST":
        s="DT "+lst[i][5:]+" TD"
    elif lst[i][:5]=="WATER":
        s="WT "+lst[i][6:]+" TW"
    elif lst[i][:4]=="FIRE":
        s="FR "+lst[i][5:]+" RF"
    lst2.append(s)
    s=""
for i in range(len(lst2)):
    a=lst2[i]
    mas=a.split(" ")
    for j in range(len(mas)):
        slovo=mas[j]
        if mas[j] in ten:
            k=int(mas[j])-1
            mas[j]=lst2[k]
    a=" ".join(mas)
    lst2[i]=a
if (lst2[-1].replace(" ","")==otvet):
    print("OK")
else:
    print("NOT OKAY")
