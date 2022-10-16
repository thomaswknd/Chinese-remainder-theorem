print("\n\nChinese remainder theorem\n\n")
def enter():
    st = ""
    lst = list()
    while True:
     st = input("Write tuple like '10 5'   ")
     r = tuple(st.split())
     if (len(r) > 2):
         raise TypeError
     lst.append(r)
     butt = input("Write 1 for continue or write something else for end  ")
     if (butt == "1"):
         pass
     else:
         break
    return lst

def rev(Mi, m, flag):
    a = m
    b = Mi
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    if flag:
        print()
        print("q   r    x    y   a   b   x2   x1   y2   y1")
        print(f"-   -    -    -  {a} {b}   1    0    0     1")
    while (b != 0):
        q = a // b
        r = a % b
        x = x2 - q*x1
        y = y2 - q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
        if flag:
            print(f"{q}   {r}   {x}   {y}   {a}   {b}   {x2}   {x1}   {y2}   {y1}")
    if flag:
        print(y2)
        print()
        print()
    return y2


def calcM(l):
    n = len(l)
    M = 1
    for j in range(n):
        M *= int(l[j][1]) 
    return M

def calc(l, flag):
    x = 0
    n = len(l)
    M = 1
    M = calcM(l)
    for i in range(n):
        a = int(l[i][0])
        m = int(l[i][1])
        Mi = int(M/m)
        y = rev(Mi, m, flag)
        x += a*Mi*y
    return x

def ans(l, flag):
    x = calc(l, flag)
    print("Answer is ", x)

    if (x < 0):
        while x < 0:
            x += calcM(l)
        print("Positive answer is ", x)

ch = input("Write 1 for enter own values or write something else for enter l list  ")

if ch == "1":
    l = enter()
else:
    l = [('5','7'), ('3','11'), ('10','13')]  # x = 5 mod 7
flag = bool(int(input("Do you want tables?\n Write 1 for output with them or write 0 for else  ")))
ans(l, flag)

