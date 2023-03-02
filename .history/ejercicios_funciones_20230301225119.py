#Crear una funcion que reciba la lista de ciudades y clasificarlos
#por la cntidad de habitantes de menor a mayor

ciudades =[
    {
        'nombre': 'Tumbes',
        'habitantes': 500000
    },
    {
        'nombre': 'Arequipa',
        'habitantes': 800000
    },
    {
        'nombre': 'Loreto',
        'habitantes': 10000
    },
]

def ordenarCiudades(lista_ciudades):
    for ciudad in lista_ciudades:
        print(ciudad['habitantes'])
        if ciudad['habitantes'] == ciudad['nombre

ordenarCiudades(ciudades)