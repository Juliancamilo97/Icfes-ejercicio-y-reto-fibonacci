def recur_fibo( n: int ):
    sucesion=[0,1,1]
    if n<3:
        return sucesion[0:n]
    else:
        for i in range(n-3):
            numero=sucesion[i+1]+sucesion[i+2]
            sucesion.append(numero)
    return sucesion

def iniciar_aplicacion( n : int ):
    return [x**3 for x in recur_fibo(n)]


print(recur_fibo(10))
print(iniciar_aplicacion(10))