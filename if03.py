def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
     Katta va kichik o'rtasidagi sonni aniqlang.
     Args:
         a: Birinchi raqam.
         b: ikkinchi raqam.
         c: Uchinchi raqam.
     Qaytaradi:
         int: javobni qaytarish.
     """

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return None  # yoki boshqa bir qiymat, misol uchun -1
print(main(1,2,4))    