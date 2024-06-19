def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: División por cero no permitida."
    return x / y

def calculator():
    print("Selecciona una operación:")
    print("1. Suma 4")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        choice = input("Ingresa el número de la operación (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor ingresa números válidos.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error: División por cero no permitida.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
            