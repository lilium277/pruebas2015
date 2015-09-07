def porcentaje(hombres, mujeres):
    """
    >>> porcentaje(10,5)
    [66, 33]
    """
    totalAlumnos = hombres + mujeres
    porHombres = (hombres * 100) / totalAlumnos
    porMujeres = (mujeres * 100) / totalAlumnos
    
    return [porHombres, porMujeres]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
