# inicio de proyecto final
def pedir_texto (mensaje):
    dato = input(mensaje).strip()
    while dato == "":
        print("Error, no puede quedar vacío")
        dato = input(mensaje). strip()
    return dato
def pedir_numero (mensaje):
    while True :
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print(" Error: Debe ingresar un número válido")
def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)
nombre = pedir_texto("Ingrese su nombre: ")
apellido = pedir_texto("Ingrese su apellido: ") 
edad = pedir_numero("Ingrese su edad: ")
estatura = pedir_numero("Ingrese su estatura: ")
peso = pedir_numero("Ingrese su peso: ")
imc = calcular_imc(peso, estatura)
print("Hola", nombre, apellido, "su IMC es:", imc)
if imc < 18.5:
    print("Está por debajo del peso")
elif imc < 25:
    print("Está en peso normal")
else:
    print("Está por encima del peso")