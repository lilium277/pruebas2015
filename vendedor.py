def vendedor(venta1, venta2, venta3):
    """
    >>> vendedor(3000,4500,2500)
    [1000.0, 2000.0]
    """
    sueldoBase = 1000
    comision = 0.10
    
    comisionTotal = (venta1 * comision + venta2 * comision + venta3 * comision)
    sueldoTotal = (sueldoBase + comisionTotal)
    return [comisionTotal, sueldoTotal]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
