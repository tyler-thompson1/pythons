import matplotlib.pyplot as plt
filex = open('/Users/tylerthompson/desktop/Thisx','r')
filey=open('/Users/tylerthompson/desktop/Thisy','r')
xvals = []
yvals = []
for line in filex:
    xvals.append(line.rstrip('\r\n'))
for line in filey:
    yvals.append(line.rstrip('\r\n'))
#**** Everything above is just to get the data in the right format****#
a=0
b=0
for i in range(len(xvals)):
    if a>float(xvals[i]):
        a=float(xvals[i])
for i in range(len(yvals)):
    if b>float(yvals[i]):
        b=float(yvals[i])
c=min([a,b])
#****This normalizes the data by finding the largest negative number****#
mat=[[0 for col in range(500)] for row in range(500)]
n=0
m=0
for i in range(len(xvals)):
    n=0
    m=0
    while n<round((float(xvals[i])+abs(c))/10) :
        n=n+1
    while m<round((float(yvals[i])+abs(c))/10) :
        m=m+1
    mat[n][m]=mat[n][m]+1
    #print n,m,mat[n][m]
plt.imshow(mat, cmap='hot', interpolation='nearest')
plt.show()
