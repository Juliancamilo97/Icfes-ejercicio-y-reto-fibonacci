import pandas as pd

def lista_cuadrados(data)-> dict:
    lista=data['Resultados'].values
    valores_erroneos=[]
    enteros_positivos= filter(lambda numero: numero if isinstance(numero, int) and numero > 0 else valores_erroneos.append(numero), lista)
    resultado= list(map(lambda numero: numero**2, enteros_positivos))
    
    diccionario_analisis={}
    
    diccionario_analisis['parametros']=resultado
    diccionario_analisis['cantidad_errores']=len(valores_erroneos)
    diccionario_analisis['errores']= valores_erroneos
    
    return diccionario_analisis

data = {"Resultados": [1, 2, 3, 4, 5, 6, 7, -2, -3, 4.9, "No hay registro", " "], 
        "ID": [5595, 2603, 4865, 1502, 7191, 6341, 8141, 4620, 5333, 2725, 8497, 8197], 
        "SEXO": ["F", "F", "F", "M", "M", "M", "M", "F", "M", "F", "M", "M"]}

print(lista_cuadrados(pd.DataFrame(data)))