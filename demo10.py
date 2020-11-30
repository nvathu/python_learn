#


def swap(a,b):
    tmp = a[:]
    a[:] = b
    b[:] = tmp
    

def main():
    a = [1]
    b = [2]
    swap(a,b)
    print(a)
    print(b)
    
if __name__ == "__main__":
    main()