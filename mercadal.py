import json

with open('path/to/json/file') as f:
    data = json.loads(f.read())
f.close()

def rotul_2666():
    return (data['ListaEESSPrecio'][92]['Rótulo'])
def direccio_2666():
    return (data['ListaEESSPrecio'][92]['Dirección'])
def benzina_2666():
    return (data['ListaEESSPrecio'][92]['Precio Gasolina 95 E5'])
def dieselA_2666():
    return (data['ListaEESSPrecio'][92]['Precio Gasoleo A'])
def dieselB_2666():
    return (data['ListaEESSPrecio'][92]['Precio Gasoleo B'])
def dieselPremium_2666():
    return (data['ListaEESSPrecio'][92]['Precio Gasoleo Premium'])
def GLP_2666():
    return (data['ListaEESSPrecio'][92]['Precio Gases licuados del petróleo'])

mercadal_2666 = {
    'rotul' : rotul_2666(),
    'direccio' : direccio_2666(),
    'benzina' : benzina_2666(),
    'dieselA' : dieselA_2666(),
    'dieselB' : dieselB_2666(),
    'dieselPremium' : dieselPremium_2666(),
    'GLP': GLP_2666()
}

def rotul_2645():
    return (data['ListaEESSPrecio'][91]['Rótulo'])
def direccio_2645():
    return (data['ListaEESSPrecio'][91]['Dirección'])
def benzina_2645():
    return (data['ListaEESSPrecio'][91]['Precio Gasolina 95 E5'])
def dieselA_2645():
    return (data['ListaEESSPrecio'][91]['Precio Gasoleo A'])
def dieselB_2645():
    return (data['ListaEESSPrecio'][91]['Precio Gasoleo B'])
def dieselPremium_2645():
    return (data['ListaEESSPrecio'][91]['Precio Gasoleo Premium'])
def GLP_2645():
    return (data['ListaEESSPrecio'][91]['Precio Gases licuados del petróleo'])

mercadal_2645 = {
    'rotul' : rotul_2645(),
    'direccio' : direccio_2645(),
    'benzina' : benzina_2645(),
    'dieselA' : dieselA_2645(),
    'dieselB' : dieselB_2645(),
    'dieselPremium' : dieselPremium_2645(),
    'GLP': GLP_2645()
}

def rotul_13267():
    return (data['ListaEESSPrecio'][90]['Rótulo'])
def direccio_13267():
    return (data['ListaEESSPrecio'][90]['Dirección'])
def benzina_13267():
    return (data['ListaEESSPrecio'][90]['Precio Gasolina 95 E5'])
def dieselA_13267():
    return (data['ListaEESSPrecio'][90]['Precio Gasoleo A'])
def dieselB_13267():
    return (data['ListaEESSPrecio'][90]['Precio Gasoleo B'])
def dieselPremium_13267():
    return (data['ListaEESSPrecio'][90]['Precio Gasoleo Premium'])
def GLP_13267():
    return (data['ListaEESSPrecio'][90]['Precio Gases licuados del petróleo'])


mercadal_13267 = {
    'rotul' : rotul_13267(),
    'direccio' : direccio_13267(),
    'benzina' : benzina_13267(),
    'dieselA' : dieselA_13267(),
    'dieselB' : dieselB_13267(),
    'dieselPremium' : dieselPremium_13267(),
    'GLP': GLP_13267()
}