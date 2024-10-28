liczba1 = float(input("Wprowadź pierwszą liczbę: "))
liczba2 = float(input("Wprowadź drugą liczbę: "))

if liczba1 > liczba2:
    print(f"Liczba {liczba1} jest większa niż {liczba2}.")
elif liczba2 > liczba1:
    print(f"Liczba {liczba2} jest większa niż {liczba1}.")
else:
    print("Obie liczby są równe.")