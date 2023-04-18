def Z(i):
    global gl_y
    global gl_x
    a=gl_y
    b=gl_x
    if i==1:
        gl_y, gl_x=n+1-b, a
    else:
        for i in range(3):
            gl_y, gl_x=n+1-b, a
            a=gl_y
            b=gl_x

def X(i):
    global gl_z
    global gl_y
    a=gl_z
    b=gl_y
    if i==1:
        gl_y, gl_z=a, n+1-b
    else:
        for i in range(3):
            gl_y, gl_z=a, n+1-b
            a=gl_y
            b=gl_x

def Y(i):
    global gl_x
    global gl_z
    a=gl_x
    b=gl_z
    if i==1:
        gl_x, gl_z=a, n+1-b
    else:
        for i in range(3):
            gl_x, gl_z=a, n+1-b
            a=gl_y
            b=gl_x
with open("C://test.txt","r") as f:
    n,m=map(int, f.readline().split())
    gl_x, gl_y, gl_z = map(int, f.readline() .split())
    #print(n,m)
    #print(gl_x, gl_y, gl_z)
    #(2, 1, 3) - (4, 2, 3)
    #(1, 2, 3) - (3, 1, 3)
    #y2=x1
    #x2=n+1-y1

    for i in range(m):
        s=f.readline()
        if s[0]=="X":
            mas=s[2:].split()
            X(int(mas[len(mas)-1]))
                
        elif s[0]=="Y":
            mas=s[2:].split()
            Y(int(mas[len(mas)-1]))
                
        elif s[0]=="Z":
            mas=s[2:].split()
            Z(int(mas[len(mas)-1]))
                    
print(gl_x, gl_y, gl_z)
