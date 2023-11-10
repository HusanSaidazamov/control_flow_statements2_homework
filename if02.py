def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
     Raqamlarning eng kichigini toping.
     Args:
         a: Birinchi raqam.
         b: ikkinchi raqam.
         c: Uchinchi raqam.
     Qaytaradi:
         int: javobni qaytarish.
     """
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
print(main(5,4,2)) 
