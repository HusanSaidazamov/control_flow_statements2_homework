def main(n):
    #if06 xato 
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    # Besh xonali raqamning eng katta raqamining indeksini topish
    # Besh xonali raqamning eng katta raqamining indeksini topish
    a = n // 10000
    b = (n // 1000) % 10
    c = (n // 100) % 10
    d = (n // 10) % 10
    e = n % 10

    if a >= b and a >= c and a >= d and a >= e:
        return 5
    elif b >= c and b >= d and b >= e:
        return 4
    elif c >= d and c >= e:
        return 3
    elif d >= e:
        return 2
    else:
        return 1

n=76514
Z= main(n)
print(n,Z)