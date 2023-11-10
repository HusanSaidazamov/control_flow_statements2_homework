def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
     Tselsiy bo'yicha sizga berilgan quyidagi harorat shartlariga muvofiq xabarni ko'rsating:
     Elif iboralaridan foydalaning.
     Temp<0: "Muzlamoqda"
     Harorat 1-10: "Juda sovuq"
     Harorat 11-20: "Sovuq"
     Harorat 21-30: "Oddiy"
     Harorat 31-40: "Issiq"
     Harorat >40: "Juda issiq"
     Args:
         harorat: Tselsiy bo'yicha harorat.
     Qaytaradi:
         str: javobni qaytarish.
        """
    if temp < 0:
        return "Freezing"
    elif 0 <= temp <= 10:
        return "Very Cold"
    elif 11 <= temp <= 20:
        return "Cold"
    elif 21 <= temp <= 30:
        return "Normal"
    elif 31 <= temp <= 40:
        return "Hot"
    else:
        return "Very Hot"                   

temp= 14
Z= main(temp)
print(Z)