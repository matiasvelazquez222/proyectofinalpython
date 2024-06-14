import random 

import json

def alta_ticket():
   
    print("\nINGRESE LOS DATOS DE SU NUEVO TICKET\n")
    
    nombre = input("INGRESE SU NOMBRE: ")
    sector = input("INGRESE SU SECTOR: ")
    asunto = input("INGRESE SU ASUNTO: ")
    problema = input("INGRESE SU PROBLEMA: ")

    datos = {
    "nombre": nombre,
    "sector": sector,
    "asunto": asunto,
    "problema":problema,
            }
   
    numeroazar=random.randint(1000, 9999)
   
    nombrejson=f"{numeroazar}.json"
    
    with open(nombrejson, 'w') as archivoj:
        json.dump(datos, archivoj, indent=4)
    print(datos)
    
    print(f"guarde su numero de ticket {numeroazar}")


def ver_ticket():
    
    numero_ticket=int(input("INGRESE SU NUMERO DE TICKET: "))
    
    nombre_json_ticket=f"{numero_ticket}.json"
    print(f"DATOS CARGADOS DE JSON CON EL NUMERO DE TICKET: {numero_ticket}")
    
    with open(nombre_json_ticket,'r') as lecturaj:
        data= json.load(lecturaj) 
        print(json.dumps(data,indent=4))      


n1=True

while n1 ==True :
    print("BIENVENIDOS AL GENEREADOR DE TICKES!")
    print("\nOPCION 1: GENERAR TICKET: ")
    print("OPCION 2: LEER TICKET")
    print("opcion 3: SALIR")
    opcion = int(input("INGRESE UNA OPCION : "))
    
    if opcion == 1:
        
        n2='s'
        while n2=='s':
         
         alta_ticket()
         n2=input("¿DESEA GENERAR OTRO TICKET? (s/n)")
         if n2=='s':
            n2=='s'
         else:
            
            n1=True
         
    if opcion == 2:
        ver_ticket()
        ticket2 = input("\nDESEA LEER OTRO TICKET? (s/n)")
        if ticket2 == 's':
         ver_ticket()
        else:
         n1=True
     
    if opcion == 3:
        n1=False
    
    else:
        print("OPCION INCORRECTA")
        n1=True