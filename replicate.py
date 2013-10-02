import math

a=13.6775
b=13.6775
c=7.5240

file_out=open('mordenita.xyz','w')
n=5
m=5
l=5
file_out.write(str(n*m*l*24)+'\nHeNeArKr\n')


with open('posiciones.txt','r') as f:
    lines=f.readlines()


aux=b*math.sin(math.pi*(90.0-82.8211)/180)

for i in range(n):
    for j in range(m):
        for k in range(l):
            for line in lines:
                linea=line.split()
                x=float(linea[1])+a*float(i)+aux*float(j)
                y=float(linea[2])+b*float(j)
                z=float(linea[3])+c*float(k)
                x_str=str(x)+' '
                y_str=str(y)+' '
                z_str=str(z)+'\n'
                if int(linea[0])<=16:
                    if int(linea[0])%2==1:
                        nombre='He '
                    else:
                        nombre='Ne '
                else:
                    if int(linea[0])%2==1:
                        nombre='Ar '
                    else:
                        nombre='Kr '
                file_out.write(nombre+x_str+y_str+z_str)






