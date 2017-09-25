from sys import stdin

for line in stdin:
    arr=list(map(int,line.split()))[1:]
    length=len(arr)
    jolly=list()
    for i in range(1,length):
        jolly.append(abs(arr[i]-arr[i-1]))
    jolly=sorted(jolly)
    if(length != 0):
        if(length == 1):
            print("Jolly")
        elif(jolly[0]==1):
            j=1
            for i in range(1,len(jolly)):
                if((jolly[i]-jolly[i-1])!=1):
                    j=0
            if(j==0):
                print("Not jolly")
            else:
                print("Jolly")
        else:
            print("Not jolly")
