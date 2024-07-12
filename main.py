from random import randint
n=20
a=[randint(50, 150) for i in range(n)]
print(a)
M=a[0]
for x in a:
    if x>M:
        M=x
nMax=0
for i in range(1,n):
    if a[i]>a[nMax]:
        nMax=i
print("Max A[", nMax, "]=",a[nMax])
for x in a:
    if x<M:
        M=x
nMin=0
for i in range(1,n):
    if a[i]<a[nMin]:
        nMin=i
print("Min A[", nMin, "]=",a[nMin])