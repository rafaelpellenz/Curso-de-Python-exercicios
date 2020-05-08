m=float(input('Digite uma medida em metros:'))
km=m*(10**(-3))
hm=m*(10**(-2))
dam=m*(10**(-1))
dm=m*10
cm=m*(10**2)
mm=m*(10**3)

print('{} km\n{} hm\n{} dam\n{} dm\n{} cm\n{} mm'.format(km,hm,dam,dm,cm,mm))