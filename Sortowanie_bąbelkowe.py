def bubble_sort(data):
    if not isinstance(data, list):
        raise ValueError("Dane wejściowe muszą być listą.")

    if len(data) > 0 and not isinstance(data[0], (int, str)):
        raise ValueError("Wszystkie elementy w liście muszą być typu int lub str.")

    if len(data) > 1 and not all(isinstance(item, type(data[0])) for item in data):
        raise ValueError(
            "Wszystkie elementy w liście muszą być tego samego typu (np. wszystkie liczby lub wszystkie napisy).")

    n = len(data)
    if n <= 1:
        return data

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


# Testy
numbers = [8, 6, 3, 1, 99, 1, 11]
print("Przed sortowaniem liczb:", numbers)
print("Po sortowaniu liczb:", bubble_sort(numbers))

strings = ["ZS", "JS", "CSS", "ZPSB", "HTML"]
print("Przed sortowaniem napisów:", strings)
print("Po sortowaniu napisów:", bubble_sort(strings))
strings = [[], "JS", "CSS", "ZPSB", "HTML"]
print("Przed sortowaniem napisów:", strings)
print("Po sortowaniu napisów:", bubble_sort(strings))
mixed = [8, "JS", 3, "HTML"]
try:
    print(bubble_sort(mixed))
except ValueError as e:
    print(f"Błąd: {e}")

try:
    print(bubble_sort("not a list"))
except ValueError as e:
    print(f"Błąd: {e}")
