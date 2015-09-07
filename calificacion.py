def calificacion(cal1, cal2, cal3):
    """
    >>> calificacion(8,8,7)
    7
    """
    calificacion = (cal1 + cal2 + cal3) / 3
    
    return calificacion
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
