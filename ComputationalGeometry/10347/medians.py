from sys import stdin

for line in stdin:
    a,b,c=map(float,line.split())
    s=(a+b+c)/2.0
    if(s*(s-a)*(s-b)*(s-c) <= 0):
        area=-1.0
    else:
        area=(4/3)*(s*(s-a)*(s-b)*(s-c))**(1/2)
    print("%.3f" % round(area,3))
