import json

with open('path/to/json/file') as f:
    data = json.loads(f.read())
f.close()

def rotul_2580():
    return (data['ListaEESSPrecio'][175]['Rótulo'])
def direccio_2580():
    return (data['ListaEESSPrecio'][175]['Dirección'])
def benzina_2580():
    return (data['ListaEESSPrecio'][175]['Precio Gasolina 95 E5'])
def dieselA_2580():
    return (data['ListaEESSPrecio'][175]['Precio Gasoleo A'])
def dieselB_2580():
    return (data['ListaEESSPrecio'][175]['Precio Gasoleo B'])
def dieselPremium_2580():
    return (data['ListaEESSPrecio'][175]['Precio Gasoleo Premium'])
def GLP_2580():
    return (data['ListaEESSPrecio'][176]['Precio Gases licuados del petróleo'])

santLluis_2580 = {
    'rotul' : rotul_2580(),
    'direccio' : direccio_2580(),
    'benzina' : benzina_2580(),
    'dieselA' : dieselA_2580(),
    'dieselB' : dieselB_2580(),
    'dieselPremium' : dieselPremium_2580(),
    'GLP': GLP_2580()
}

def rotul_13028():
    return (data['ListaEESSPrecio'][176]['Rótulo'])
def direccio_13028():
    return (data['ListaEESSPrecio'][176]['Dirección'])
def benzina_13028():
    return (data['ListaEESSPrecio'][176]['Precio Gasolina 95 E5'])
def dieselA_13028():
    return (data['ListaEESSPrecio'][176]['Precio Gasoleo A'])
def dieselB_13028():
    return (data['ListaEESSPrecio'][176]['Precio Gasoleo B'])
def dieselPremium_13028():
    return (data['ListaEESSPrecio'][176]['Precio Gasoleo Premium'])
def GLP_13028():
    return (data['ListaEESSPrecio'][176]['Precio Gases licuados del petróleo'])

santLluis_13028 = {
    'rotul' : rotul_13028(),
    'direccio' : direccio_13028(),
    'benzina' : benzina_13028(),
    'dieselA' : dieselA_13028(),
    'dieselB' : dieselB_13028(),
    'dieselPremium' : dieselPremium_13028(),
    'GLP': GLP_13028()
}