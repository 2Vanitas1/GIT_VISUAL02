def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


def pedir_numeros():
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))
    return a, b


def main():
    print("Calculadora simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        opcion = input("\nElige una opcion (1-5): ").strip()

        if opcion == "5":
            print("Hasta luego")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opcion no valida")
            continue

        a, b = pedir_numeros()

        if opcion == "1":
            resultado = sumar(a, b)
        elif opcion == "2":
            resultado = restar(a, b)
        elif opcion == "3":
            resultado = multiplicar(a, b)
        else:
            resultado = dividir(a, b)

        print("Resultado:", resultado)


if __name__ == "__main__":
    main()
