def nuevoSalario(salario):
    """
    >>> nuevoSalario(1000)
    1250.0
    """
    aumento = 0.25
    nuevoSal = salario+(salario * aumento)
    return nuevoSal
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
