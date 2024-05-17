n=int(input())
words=[]
for i in range(n):
    words.append(input())
s=int(input())
st_w=[]
st_k=[]
for i in range(s):
    u=input().split(' ')
    st_w.append(u[0])
    st_k.append(int(u[1]))
    
e=int(input())
end_w=[]
end_k=[]
for i in range(e):
    u=input().split(' ')
    end_w.append(u[0])
    end_k.append(int(u[1]))

result=[]
st=[]
end=[]
for i in range(s):
    st1=[st_w[i], st_k[i]]
    st.append(st1)
for i in range(e):
    st1=[end_w[i], end_k[i]]
    end.append(st1)
st=sorted(st, key=lambda x: x[1])
end=sorted(end,key =lambda x: x[1])
end=end[::-1]

for i in range(len(st)):
    a=st[i][0]
    if st[i][1]>0:
        for j in range(len(end)):
            b=end[j][0]
            for l in range(n):
                if a==words[l][0] and words[l][-1]==b:
                    result.append(words[l])
                    words[l]='1'
                    st[i][1]-=1
                    end[j][1]-=1
                if st[i][1]==0 or end[j][1]==0:
                    break
            if st[i][1]==0:
                break

for i in range(len(end)):
    a=end[i][0]
    if end[i][1]>0:
        for j in range(len(st)):
            b=st[j][0]
            for l in range(n):
                if a==words[l][-1] and words[l][0]==b:
                    result.append(words[l])
                    words[l]='1'
                    st[i][1]-=1
                    end[j][1]-=1
                if st[j][1]==0 or end[i][1]==0:
                    break
            if end[i][1]==0:
                break

print(len(result))

    
    
                
        
        
