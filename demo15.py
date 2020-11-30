def drawTriangle_1(h):
    for i in range(h):
        for j in range ( h+i ):
            if (h-1)- i <= j and j <= (h-1)+i :
                print("*",end="")
            else:
                print(" ",end="")
        print()
            

def drawTriangle_2(h):
    for i in range(h):
        for j in range ((h)+i):
            if (h-1)- i == j or j == (h-1)+i or i == h -1:
                print("*",end="")
            else:
                print(" ",end="")
        print()