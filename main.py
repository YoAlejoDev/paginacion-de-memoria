import time

tamañoMemoria = int(input("Ingrese el tamaño total de la memoria: "))

process = []
processLate = []

while True:
    
    print("Ingrese la opcion de proceso que desea: ")
    opc = int(input("\n1. Escribir en la memoria \n2. Leer la memoria \n3. Eliminar procesos activos \n4. Eliminar procesos en espera \n5. Salir \n"))
    
    if opc == 5:
        break
    
    elif opc == 1:
        data = str(input("Ingrese el nombre del proceso: "))
        size = int(input("Ingrese el tamaño de los procesos: "))
        
        memoriaLibre = tamañoMemoria - len(process) 
        
        if size <= memoriaLibre:
            process.extend([data] * size)
            print("Proceso agregado perfectamente")
            print(process)
        else:
            processLate.extend([data] * size)
            print("Proceso agregado a lista de espera")
            print(processLate)
            
    elif opc == 2:
        opc2 = int(input("\n1. Leer memoria ocupada \n2. Leer memoria de procesos en espera \n"))
        
        if opc2 == 1:
            print(process)
        elif opc2 == 2:
            print(processLate)
        else:
            print("Opcion no valida")

    elif opc == 3:
        print(process)
        target = input("Ingrese el proceso activo que desea eliminar: ")
        process = [x for x in process if x != target]
        print(process)
        
        time.sleep(2)
        
        print("Agregando procesos en espera a activos...")
        
        time.sleep(2)
        
        while memoriaLibre < tamañoMemoria:
            if processLate:
                procesoNew = processLate.pop()
                process.append(procesoNew)
                memoriaLibre += 1
            else:
                print("No hay mas procesos en espera para agregar")
                break
                    
    elif opc == 4:
        print(processLate)
        target = input("Ingrese el proceso activo que desea eliminar: ")
        processLate = [x for x in processLate if x != target]
        print(processLate)
    
    