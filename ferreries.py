import json

with open('path/to/json/file') as f:
    data = json.loads(f.read())
f.close()

def rotul_2605():
    return (data['ListaEESSPrecio'][53]['Rótulo'])
def direccio_2605():
    return (data['ListaEESSPrecio'][53]['Dirección'])
def benzina_2605():
    return (data['ListaEESSPrecio'][53]['Precio Gasolina 95 E5'])
def dieselA_2605():
    return (data['ListaEESSPrecio'][53]['Precio Gasoleo A'])
def dieselB_2605():
    return (data['ListaEESSPrecio'][53]['Precio Gasoleo B'])
def dieselPremium_2605():
    return (data['ListaEESSPrecio'][53]['Precio Gasoleo Premium'])
def GLP_2605():
    return (data['ListaEESSPrecio'][53]['Precio Gases licuados del petróleo'])

ferreries_2605 = {
    'rotul' : rotul_2605(),
    'direccio' : direccio_2605(),
    'benzina' : benzina_2605(),
    'dieselA' : dieselA_2605(),
    'dieselB' : dieselB_2605(),
    'dieselPremium' : dieselPremium_2605(),
    'GLP': GLP_2605()
}