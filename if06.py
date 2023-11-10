def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
     Besh xonali sonning eng katta raqamining indeksini toping.
     Args:
         n: besh xonali raqam.
     Qaytaradi:
         int: javobni qaytarish.
     """
    # Besh xonali raqamning eng katta raqamining indeksini topish
    # Besh xonali raqamning eng katta raqamining indeksini topish
    a = n // 10000
    b = (n // 1000) % 10
    c = (n // 100) % 10
    d = (n // 10) % 10
    e = n % 10

    if a >= b and a >= c and a >= d and a >= e:
        return 0
    elif b >= c and b >= d and b >= e:
        return 1
    elif c >= d and c >= e:
        return 2
    elif d >= e:
        return 3
    else:
        return 4

n=54694
Z= main(n)
print(n,Z)