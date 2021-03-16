import json

with open('path/to/json/file') as f:
    data = json.loads(f.read())
f.close()

def rotul_13582():
    return (data['ListaEESSPrecio'][34]['Rótulo'])
def direccio_13582():
    return (data['ListaEESSPrecio'][34]['Dirección'])
def benzina_13582():
    return (data['ListaEESSPrecio'][34]['Precio Gasolina 95 E5'])
def dieselA_13582():
    return (data['ListaEESSPrecio'][34]['Precio Gasoleo A'])
def dieselB_13582():
    return (data['ListaEESSPrecio'][34]['Precio Gasoleo B'])
def dieselPremium_13582():
    return (data['ListaEESSPrecio'][34]['Precio Gasoleo Premium'])
def GLP_13582():
    return (data['ListaEESSPrecio'][34]['Precio Gases licuados del petróleo'])

esCastell_13582 = {
    'rotul' : rotul_13582(),
    'direccio' : direccio_13582(),
    'benzina' : benzina_13582(),
    'dieselA' : dieselA_13582(),
    'dieselB' : dieselB_13582(),
    'dieselPremium' : dieselPremium_13582(),
    'GLP': GLP_13582()
}