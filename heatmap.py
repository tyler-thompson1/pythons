import matplotlib.pyplot as plt
filex = open('/Users/tylerthompson/desktop/Thisx','r')
filey=open('/Users/tylerthompson/desktop/Thisy','r')
xvals = []
yvals = []
for line in filex:
    xvals.append(line.rstrip('\r\n'))
for line in filey:
    yvals.append(line.rstrip('\r\n'))
mat=[[0 for col in range(29)] for row in range(29)]
n=0
m=0
for i in range(len(xvals)):
    n=0
    m=0
    while n<round(float(xvals[i]))/100 :
        n=n+1
    while m<abs(round(float(yvals[i])))/100 :
        m=m+1
    mat[n][m]=mat[n][m]+1
    #print n,m,mat[n][m]
    #print m,n
plt.imshow(mat, cmap='hot', interpolation='nearest')
plt.show()
