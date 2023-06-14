#Code for resolving systems of equations

import numpy as np

print("Option=1: Système de 2 équations à 2 inconnues; Option=2: Système de 3 équations à 3 inconnues")
Option=int(input("Entrez votre option"))
if (Option==1):
           print("On a un système de 2 équations à 2 inconnues de la forme:")
           print("{ax+by=e")
           print("{cx+dy=f")
           print("Entrez a,b,c,d,e,f")
           a=int(input("a="))
           b=int(input("b="))
           c=int(input("c="))
           d=int(input("d="))
           e=int(input("e="))
           f=int(input("f="))
           print("Ainsi on a le système:")
           print("{"+str(a)+"x+"+str(b)+"y="+str(e))
           print("{"+str(c)+"x+"+str(d)+"y="+str(f))
           T1=np.array([[a,b],[c,d]])
           Tx=np.array([[e,b],[f,d]])
           Ty=np.array([[a,e],[b,f]])
           T2=np.array([[e],[f]])
           D=np.linalg.det(T1)
           Dx=np.linalg.det(Tx)
           Dy=np.linalg.det(Ty)
           if (D==0 and Dx==Dy==0):
               print("Le système admet une infinité de solutions")
           elif(D==0 and (Dx!=0 or Dy!=0)):
               print("Le système n'admet pas de solutions")
           else:
               B=np.linalg.inv(T1)
               R=B@T2
               x=R[0]
               y=R[1]
               print("Les solutions de ce système d'équation sont: x="+str(x)+" y="+str(y))
           
elif(Option==2):
    print("On a un système de 3 équations à 3 inconnues de la forme:")
    print("{ax+by+cz=j")
    print("{dx+ey+fz=k")
    print("{gx+hy+iz=l")
    print("Entrez a,b,c,d,e,f,g,h,i,j,k,l")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    d=int(input("d="))
    e=int(input("e="))
    f=int(input("f="))
    g=int(input("g="))
    h=int(input("h="))
    i=int(input("i="))
    j=int(input("j="))
    k=int(input("k="))
    l=int(input("l="))
    print("Ainsi on a le système:")
    print("{"+str(a)+"x+"+str(b)+"y+"+str(c)+"z="+str(j))
    print("{"+str(d)+"x+"+str(e)+"y+"+str(f)+"z="+str(k))
    print("{"+str(g)+"x+"+str(h)+"y+"+str(i)+"z="+str(l))
    T1=np.array([[a,b,c],[d,e,f],[g,h,i]])
    Tx=np.array([[j,b,c],[k,e,f],[l,h,i]])
    Ty=np.array([[a,j,c],[d,k,f],[g,l,i]])
    Tz=np.array([[a,b,j],[d,e,k],[g,h,l]])
    T2=np.array([[j],[k],[l]])
    D=np.linalg.det(T1)
    Dx=np.linalg.det(Tx)
    Dy=np.linalg.det(Ty)
    Dz=np.linalg.det(Tz)
    if (D==0 and Dx==Dy==Dz==0):
        print("Le système admet une infinité de solutions")
    elif(D==0 and (Dx!=0 or Dy!=0 or Dz!=0)):
        print("Le système n'admet pas de solutions")
    else:
        B=np.linalg.inv(T1)
        R=B@T2
        x=R[0]
        y=R[1]
        z=R[2]
        print("Les solutions de ce système d'équation sont: x="+str(x)+" y="+str(y)+" z="+str(z))
               
else:
    print("Redémarrez le programme et choisissez entre '1' et '2' pour le choix de l'option")
