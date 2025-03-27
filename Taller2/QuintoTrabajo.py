#pide una nota entre 0 y 100 e imprima la calificacion:
nota = float(input("ingrese la nota (0-100):"))
#determine la calificacion}
if nota >= 0 and nota <= 100:
    
    if 90 <= nota <= 100:
        print("Excelente")
    elif 70 <= nota < 90:
        print("Aprobado")
    elif 0 <= nota < 70:
        print("Reprobado")
else:
    print("nota fuera de rango") 

           



