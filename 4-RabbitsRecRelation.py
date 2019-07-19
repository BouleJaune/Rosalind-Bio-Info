n=35
k=2

u=[1,1]
for i in range(2,n):
    u.append(u[-2]*k+u[-1])
print(u[-1])    