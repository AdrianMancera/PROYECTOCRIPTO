import json
from pathlib import Path


def ejecutar():
    input_name = input("INTRODUCE TU NOMBRE:")
    input_password = input("INTRODUCE TU CLAVE")
    input_name = input_name.lower()
    if (check(input_name,input_password)) == False:
        print("FIN DE PROCESO CLAVE O USUARIO NO VALIDO")
        return None
    input_orden = input("QUIERES HACE UN BIZUM?¿ SI O NO:")
    if input_orden.lower() == "si":
        bizum(input_name,input_password)


def check(input_name, input_password):
        my_file = "C:\\Users\\ADRIAN\\PycharmProjects\\pythonProject18\\src\\main\\cuentas.json"

        try:
            with open(my_file, "r", encoding="utf-8",newline="") as file:
                archivo = json.load(file)
        except FileNotFoundError as ex:
            raise Exception("lectura erronea del json") from ex

        for i in archivo:
            if i["nombre"] == input_name:
               if i["clave"] == input_password:
                   print("adadq")
                   return True
               else:
                   return False
        return False

def bizum(input_name, input_password):
        destination = input("A quien quieres enviar el bizum, escriba su nombre:")
        dinero = input("Ingrese cantidad a enviar:")

        my_file = "C:\\Users\\ADRIAN\\PycharmProjects\\pythonProject18\\src\\main\\cuentas.json"

        try:
            with open(my_file, "r", encoding="utf-8", newline="") as file:
                archivo = json.load(file)
        except FileNotFoundError as ex:
            raise Exception("lectura erronea del json") from ex

        for i in archivo:
            if i["nombre"] == input_name:
                if i["balance"] > 0:
                     dinero = i["balance"] - int(dinero)
                     print(dinero)
            if i["nombre"] == destination:
                i["balance"] += int(dinero)


        jsonFile = open(my_file, "r+")
        jsonFile.write(json.dumps(archivo))





        




ejecutar()