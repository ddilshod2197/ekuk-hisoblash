def ekub(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

print("Eng katta umumiy bo'luvchi:", ekub(a, b))
