def extended_euclidean_algorithm(Mi, m, flag):
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