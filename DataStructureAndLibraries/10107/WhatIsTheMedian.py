from sys import stdin

def median(lc):
    lc.sort()
    length=len(lc)
    if(length%2 == 0):
        return((lc[(length//2)-1]+lc[length//2])//2)
    else:
        return(lc[length//2])

l=list()
for line in stdin:
    l.append(int(line))
    print(median(l))
