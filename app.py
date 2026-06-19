import time

def calcular_suma(valor_actual, incremento=10):
    return valor_actual + incremento

cancion = [
    "Achalay, desaparecer no sonó tan loco",
    "Si me achino al sonreír, pues ser feli' nos ciega un poco",
    "Achalay, desaparecer no sonó tan loco",
    "Si me achino al sonreír, pues ser feliz nos ciega un poco",
    "Achalay, desaparecer (Wuh) no sonó tan loco",
    "Si no tengo a dónde ir, llevo a mi tierra a donde toco",
    "Achalay, desaparecer no sonó tan loco",
    "No estamos tan loco', soy feliz con poco",
    "Vuelvo a tocar a mi tierra, se ven en mis ojos recuerdo' de guerra",
    "Esperando a la mala, tomándome un matе, nací pa'l combate, a mí nada me aterra",
    "Clavando la faca еn el piso, lo tuve que hacer cuando nadie lo hizo",
    "Siempre vuelvo en el momento preciso y como soy buen payador, improviso, ja",
    "Metido en la puna, contándole to' mis secreto' a la luna, cantándole al cielo canciones de cuna",
    "Vuelvo con fortuna para mi comuna, criado entre puma'",
    "Cacé de la pata al futuro, busco la luz en momentos oscuros",
    "Callo tras callo pisando más duro",
    "Joven reserva que vino del monte argentino, que afronte el destino este porte tan puro",
    "O mato y muero si es por mi bandera, me siento Cabral, clavándola afuera",
    "Voy a hacer historia el día que me muera (¡Wuh!)",
    "Salí sin caballo y gané la carrera, navegando y borrando frontera'",
    "Busco la gloria en mi vida guerrera, yo sé que después de la luz nos espera, wah",
    "No soy de aquí ni soy de allá",
    "No tengo edad ni porvenir",
    "Y ser feliz es mi color de identidad"
]

# Esta es la automatización
def iniciar_automatizacion():
    suma = 0
    linea = 0
    print("--- INICIANDO AUTOMATIZACIÓN DE DOCKER ---")
    
    while True:
        suma = calcular_suma(suma)
        
        if linea >= len(cancion):
            linea = 0
            
        print(f"[+] Suma actual: {suma} | 🎵 {cancion[linea]}")
        
        linea += 1
        time.sleep(10)

# Esto evita que el bucle arranque cuando hacemos la prueba unitaria
if __name__ == '__main__':
    iniciar_automatizacion()
#cambio codigo para prueba unitaria