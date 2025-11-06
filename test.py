age=[1,2,3,4,5]
length=[85,160,215,250,275]

n=len(age)
x =sum(age)
xi2=sum([x**2 for x in range])
xi3=sum([x**3 for x in age])
xi4=sum([x**4 for x in age])

y=sum([length])
xiyi=sum([age[i]*length[i] for i in range(n)])
xi2yi=sum((age[i]**2)*length[i] for i in range(n))

