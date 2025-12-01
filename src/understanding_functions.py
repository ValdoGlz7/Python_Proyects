"""
    COMO ABRIR ARCHIVOS, TESTING (RUFF CHECK) COMO CONSUMIR API, DART Y FLUTTER
"""
"""
    Docstring for understanding_functions
    Las funciones som bloques de codigo diseñadas para realizar
    una tarea especifica.
    cuando queramos realziar una tareaa que se ha definido en una funcion
    simplemente lo que hay que hacer es llamar elnombredelafuncion
    que queremos ejecutar
    "Definicioon de una funcion" o "sintaxis general de una funcion"
"""
def greeting_paulo():
    """
        Docstring for greeting_paulo
        Esta funcion saluda a paulo
    """
    print("Hola Paulo")

"""
    Vamos a hacer una funcion que pida al usuario el
    first_name, second_name y last_name
    la funcion debe regresar el nombre completo
"""
#La funcion tiene 3 parametros
def create_full_name(first_name, last_name, middle_name=""):
    """
        Docstring for create_full_name
        Esta funcion genera el full name
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name
user_first_name = input("Please enter your first name: ").strip().lower()
user_middle_name = input ("Please enter your middle name: ").strip().lower()
user_last_name  =input("Please enter your last name: ").strip().lower()
#Argumentos clave = Keyword arguments
full_name_key = create_full_name(
                                last_name = user_last_name, 
                                first_name = user_first_name, 
                                middle_name = user_middle_name
                                )
#Argumentos posicionales = Positional arguments
print(create_full_name(
    user_first_name,
    user_middle_name, 
    user_last_name
    ))

generated_full_name = create_full_name(
    user_first_name, 
    user_middle_name,
    user_last_name
    )
print(generated_full_name)
#Args, kwargs
#Como explorar archivos (Diccionarios, .txt, csv, jsom)
#args por consola (sys)
#cli - command linear interface
#oop - oriented object programming
#testing - ruff,  pytest
"""
   Los args y kwargs son parametros especiales
   que se utilizan en la definicion de funciones
"""