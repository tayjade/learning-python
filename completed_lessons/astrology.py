m = input("What month were you born?\n").lower()

d = int(input("What date were you born?\n"))

astro_sign = ""

if m == "january":
    if d <19:
        astro_sign = "Capricorn"
    else:
        astro_sign = "Aquarius"
elif m == "february":
    if d <18:
        astro_sign = "Aquarius"
    else:
        astro_sign = "Pisces"
elif m == "march":
    if d< 20:
        atro_sign = "Pisces"
    else:
        astro_sign = "Aries"
elif m == "april":
    if d <19:
        astro_sign = "Aries"
    else:
        astro_sign = "Taurus"
elif m == "may":
    if d< 20:
        astro_sign = "Taurus"
    else:
        astro_sign = "Gemini"
elif m == "june":
    if d< 21:\
        astro_sign = "Gemini"
    else:
        astro_sign = "Cancer"
elif m == "july":
    if d< 22:
        astro_sign = "Cancer"
    else: 
        astro_sign = "Leo"
elif m == "august":
    if d< 22:
        astro_sign = "Leo"
    else:
        astro_sign = "Virgo"
elif m == "september":
    if d< 22:
        astro_sign = "Virgo"
    else: 
        astro_sign = "Libra"
elif m == "october":
    if d< 23:
        astro_sign = "Libra"
    else:
        astro_sign = "Scorpio"
elif m == "november":
    if d< 21:
        astro_sign = "Scorpio"
    else:
        astro_sign = "Sagittarius"
elif m == "december":
    if d< 21:
        astro_sign = "Sagittarius"
    else: 
        astro_sign = "Capricorn"
        
print(astro_sign)
