import json

with open('path/to/json/file') as f:
    data = json.loads(f.read())
f.close()


def rotul_2669():
    return (data['ListaEESSPrecio'][0]['Rótulo'])


def direccio_2669():
    return (data['ListaEESSPrecio'][0]['Dirección'])


def benzina_2669():
    return (data['ListaEESSPrecio'][0]['Precio Gasolina 95 E5'])


def dieselA_2669():
    return (data['ListaEESSPrecio'][0]['Precio Gasoleo A'])


def dieselB_2669():
    return (data['ListaEESSPrecio'][0]['Precio Gasoleo B'])


def dieselPremium_2669():
    return (data['ListaEESSPrecio'][0]['Precio Gasoleo Premium'])


def GLP_2669():
    return (data['ListaEESSPrecio'][0]['Precio Gases licuados del petróleo'])


alaior_2669 = {
    'rotul': rotul_2669(),
    'direccio': direccio_2669(),
    'benzina': benzina_2669(),
    'dieselA': dieselA_2669(),
    'dieselB': dieselB_2669(),
    'dieselPremium': dieselPremium_2669(),
    'GLP': GLP_2669()
}


def rotul_2591():
    return (data['ListaEESSPrecio'][1]['Rótulo'])


def direccio_2591():
    return (data['ListaEESSPrecio'][1]['Dirección'])


def benzina_2591():
    return (data['ListaEESSPrecio'][1]['Precio Gasolina 95 E5'])


def dieselA_2591():
    return (data['ListaEESSPrecio'][1]['Precio Gasoleo A'])


def dieselB_2591():
    return (data['ListaEESSPrecio'][1]['Precio Gasoleo B'])


def dieselPremium_2591():
    return (data['ListaEESSPrecio'][1]['Precio Gasoleo Premium'])


def GLP_2591():
    return (data['ListaEESSPrecio'][1]['Precio Gases licuados del petróleo'])


alaior_2591 = {
    'rotul': rotul_2591(),
    'direccio': direccio_2591(),
    'benzina': benzina_2591(),
    'dieselA': dieselA_2591(),
    'dieselB': dieselB_2591(),
    'dieselPremium': dieselPremium_2591(),
    'GLP': GLP_2591()
}


def rotul_2590():
    return (data['ListaEESSPrecio'][2]['Rótulo'])


def direccio_2590():
    return (data['ListaEESSPrecio'][2]['Dirección'])


def benzina_2590():
    return (data['ListaEESSPrecio'][2]['Precio Gasolina 95 E5'])


def dieselA_2590():
    return (data['ListaEESSPrecio'][2]['Precio Gasoleo A'])


def dieselB_2590():
    return (data['ListaEESSPrecio'][2]['Precio Gasoleo B'])


def dieselPremium_2590():
    return (data['ListaEESSPrecio'][2]['Precio Gasoleo Premium'])


def GLP_2590():
    return (data['ListaEESSPrecio'][2]['Precio Gases licuados del petróleo'])


alaior_2590 = {
    'rotul': rotul_2590(),
    'direccio': direccio_2590(),
    'benzina': benzina_2590(),
    'dieselA': dieselA_2590(),
    'dieselB': dieselB_2590(),
    'dieselPremium': dieselPremium_2590(),
    'GLP': GLP_2590()
}