def reserve(n):
    reserveNum = 0
    while n > 0 :
        reserveNum = (reserveNum * 10) + (n % 10)
        n= n // 10
    
    return reserveNum


def isSymmetry(n):
    reservenum=reserve(n)
    return reservenum==n
        
      
def main():
     n = int(input("Enter a number: "))
     t = reserve(n)
     print("Revert number is ",t)
     if(isSymmetry(n)):
        print(n,"is a Symmetrical number")
     else:
        print(n,"is not a Symmetrical number") 
     
   
    
if __name__ == "__main__":
    main()