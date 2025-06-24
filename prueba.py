usuarios: []

def ValidarGenero():

    while True:
        genero = input("ingrese el genero del usuario:")
        if genero == "M":
            return genero
        elif genero == "F":
            return genero
        elif genero == "mujer":
            print("debe ingresar solamente M o F. intente nuevamente")
            continue
        elif genero == "hombre":
            print("debe ingresar solamente M o F. intente nuevamente")
            continue


def validarUsuario():
    while True:
        nombre = input ("ingrese el nombre de usuario:").strip()
        nombreexistente = True
        break
    if nombre == "":
        print("No puede dejar la casilla vacia")
    elif nombreexistente == False:
        return nombre

def validarContraseña():
    while True:
        contraseña = input("ingrese la contraseña:")
        if len(contraseña)>= 8 and contraseña.isalnum():
            print("Contraseña invalida")
        else:
            print("Contraseña valida")
            continue
        


def nuevoUsuario():
    
    nombre = validarUsuario()
    genero = ValidarGenero()
    contraseña  = validarContraseña()
    AgregarUsuarios ={

        "Nombre" :nombre,
        "Genero" :genero,
        "contraseña" :contraseña
    
    }


    usuarios.append(nuevoUsuario)

    
def buscarusuario():
    while True:
        busquedaUsuario = input("ingrese el nombre del usuario:").strip()
        nombreexistente = True
        
        if busquedaUsuario == "" :
    
         for i in busquedaUsuario:
              if i['nombre'].lower() == busquedaUsuario.lower():
                    print(f"el genero del usuario es: {i["genero"]} - la contraseña del usuario es: {i["contraseña"]}")
                    nombreexistente = False

def eliminarUsuario():
   while True:
    
    Eliminar = input("ingrese el usuario a eliminar:")
    for i in usuarios:
        if i["nombre"] == Eliminar:
            usuarios.remove(i['nombre'])
            usuarios.remove(i['genero'])
            usuarios.remove(i['contraseña'])
            print("usaurio eliminado con exito")
            continue



while True :
    print("menu de usuaios")
    print("[1] - ingrese un usuario")
    print("[2] - buscar un usuario")
    print("[3] - eliminar un usuario")
    print("[4] - salir")
    opc = int(input("eligue una opcion:"))
    
    
    if opc == 1 :
        usuarios = nuevoUsuario()
        print("Usuario agregado con existo!!!")
            
    elif opc == 2:
       buscarusuario() 
    elif opc == 3:
        eliminarUsuario()
    elif opc == 4:
        print ("Programa terminando.....")
        break
    else:
        print("ingrese una opcion valida")
