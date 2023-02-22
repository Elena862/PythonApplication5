a=int(46275)
b=a//10000#des_tic
b1=a//1000%10#tisiacha
b2=a//100%10#sotni
b3=a//10%10#sdesiatki
b4=a%10#edinitca
chislo=float(((b3**b4)*b2)/(b-b1))
print(b)
print(b1)
print(b2)
print(b3)
print(b4)
print(chislo)

