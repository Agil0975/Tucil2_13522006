# import matplotlib.pyplot as plt
# 
# # fungsi yang mengembalikan titik tengah antara dua titik
# def midpoint(p1, p2) -> tuple: 
#     return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
# 
# # fungsi yang mengembalikan list of midpoint diantara dua titik pada sebuah list of titik
# def list_of_midpoint(p : list) -> list:
#     hasil = []
#     for i in range(len(p) - 1):
#         hasil.append(midpoint(p[i], p[i + 1]))
#     return hasil
# 
# A = [(-10,0),(-7,7),(0,10),(7,7),(10,0)]
# B = list_of_midpoint(A)
# C = list_of_midpoint(B)
# D = list_of_midpoint(C)
# E = list_of_midpoint(D)
# 
# x = []
# x.append(A[0])
# x.append(B[0])
# x.append(C[0])
# x.append(D[0])
# x.append(E[0])
# 
# y = []
# y.append(E[-1])
# y.append(D[-1])
# y.append(C[-1])
# y.append(B[-1])
# y.append(A[-1])
# 
# 
# plt.plot([x[0] for x in A], [x[1] for x in A], color='k')
# plt.plot([x[0] for x in B], [x[1] for x in B], color='k')
# plt.plot([x[0] for x in C], [x[1] for x in C], color='k')
# plt.plot([x[0] for x in D], [x[1] for x in D], color='k')
# plt.plot([x[0] for x in E], [x[1] for x in E], color='k')
# plt.scatter([x[0] for x in A], [x[1] for x in A], c='r')
# plt.scatter([x[0] for x in B], [x[1] for x in B], c='g')
# plt.scatter([x[0] for x in C], [x[1] for x in C], c='b')
# plt.scatter([x[0] for x in D], [x[1] for x in D], c='m')
# plt.scatter([x[0] for x in E], [x[1] for x in E], c='y')
# 
# 
# 
# plt.plot([i[0] for i in x], [i[1] for i in x], c = 'cyan')
# plt.plot([i[0] for i in y], [i[1] for i in y], c = 'yellow')
# plt.scatter(x[0][0],x[0][1], c='r')
# plt.scatter(x[1][0],x[1][1], c='g')
# plt.scatter(x[2][0],x[2][1], c='b')
# plt.scatter(x[3][0],x[3][1], c='m')
# plt.scatter(x[4][0],x[4][1], c='y')
# plt.scatter(y[0][0],y[0][1], c='y')
# plt.scatter(y[1][0],y[1][1], c='m')
# plt.scatter(y[2][0],y[2][1], c='b')
# plt.scatter(y[3][0],y[3][1], c='g')
# plt.scatter(y[4][0],y[4][1], c='r')
# 
# plt.show()

a = (2,3)
c = [(4,5)]
b = [(5,4)]
d = [(6,7)]
#b.append(a)
#d.append(c)
print(b + d)
print(b)
print(d)