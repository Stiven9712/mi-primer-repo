calificaciones = (3.5,4.0,2.8,5.0,4.5)
print ("calificaciones:" , calificaciones )
promedio = sum (calificaciones)/len(calificaciones)
print("promedio: ",promedio )
print("nota mas alta:", max(calificaciones))
print("nota mas baja:", min(calificaciones))
if 5.0 in calificaciones:
    print("al menos un estudiante saco 5.0")
else:
    print("nadie saco 5.0.")
