def quick_sort(data):
    # Walidacja typu danych
    if not isinstance(data, list):
        raise ValueError("Dane wejściowe muszą być listą.")

    if len(data) > 0 and not isinstance(data[0], (int, str)):
        raise ValueError("Wszystkie elementy w liście muszą być typu int lub str.")

    if len(data) > 1 and not all(isinstance(item, type(data[0])) for item in data):
        raise ValueError(
            "Wszystkie elementy w liście muszą być tego samego typu (np. wszystkie liczby lub wszystkie napisy).")

    # Funkcja rekurencyjna do sortowania szybkiego
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]  # Wybieramy pierwszy element jako pivot
        lesser = [item for item in data[1:] if item <= pivot]
        greater = [item for item in data[1:] if item > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


# Testy funkcji
if __name__ == "__main__":
    # Test z liczbami
    numbers = [8, 6, 3, 1, 99, 1, 11]
    print("Przed sortowaniem liczb:", numbers)
    print("Po sortowaniu liczb:", quick_sort(numbers))

    # Test z napisami
    strings = ["ZS", "JS", "CSS", "ZPSB", "HTML"]
    print("Przed sortowaniem napisów:", strings)
    print("Po sortowaniu napisów:", quick_sort(strings))

    # Test z pustą listą
    empty_list = []
    print("Przed sortowaniem pustej listy:", empty_list)
    print("Po sortowaniu pustej listy:", quick_sort(empty_list))

    # Test z niejednorodnymi danymi (spowoduje błąd walidacji)
    mixed = [8, "JS", 3, "HTML"]
    try:
        print(quick_sort(mixed))
    except ValueError as e:
        print(f"Błąd: {e}")

    try:
        print(quick_sort("not a list"))
    except ValueError as e:
        print(f"Błąd: {e}")
