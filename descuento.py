def descuento(prod1, prod2, prod3):
    """
    >>> descuento(3000,4500,2500)
    1500.0
    """
    venta = prod1 + prod2 + prod3
    descuento = 0.15
    total = venta * descuento
    
    return total
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
