def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
     Agar raqamlar teng bo'lsa, nolni qaytaring, agar ular teng bo'lmasa, kattasini qaytaring.
     Args:
         a: Birinchi raqam.
         b: ikkinchi raqam.
     Qaytaradi:
         int: javobni qaytarish.
     """
    if a == b:
        return 0
    elif a > b:
        return a
    else:
        return b
a = 5
b = 3

javob = main(a, b)
print(javob)  # 5    