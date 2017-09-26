if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        a,b,c=map(int,input().split())
        print("Case ",i+1,": ",end="",sep="")
        if(a<=0 or b<=0 or c<=0):
            print("Invalid", sep="")
        elif((a+b)<=max(a,b,c) or (b+c) <= max(a,b,c) or (c+a) <=max(a,b,c)):
            print("Invalid", sep="")
        elif(a==b and b==c):
            print("Equilateral", sep="")
        elif(a==b or b==c or c==a):
            print("Isosceles", sep="")
        else:
            print("Scalene", sep="")
