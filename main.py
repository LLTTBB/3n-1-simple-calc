import matplotlib.pyplot as plt

def collatz(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

n = int(input("Ingresa un número: "))
sequence = collatz(n)
x = range(len(sequence))

plt.plot(x, sequence)
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.title("Secuencia de 3n+1 para n={}".format(n))
plt.show()

# Guardar la secuencia en un archivo de texto
file_name = "secuencia_{}.txt".format(n)
with open(file_name, "w") as file:
    for num in sequence:
        file.write(str(num) + "\n")

print("La secuencia se ha guardado en el archivo:", file_name)
