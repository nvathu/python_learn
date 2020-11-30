def main():
    num=int(input("enter a number "))
    if num % 2==0:
        print("even")
        print("Even value",num)
    else:
        print("odd")
        if num < 0:
            print("Negative number")
        elif num == 0:
            print("Zero")
        else :
            print("Positive number")
    
    
if __name__ == "__main__":
    main()