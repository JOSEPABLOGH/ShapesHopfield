# José Pablo Galindo Hernández A01276079

M = 8          
N = 5  

FIGURAS = [
    ["..#..",      
     ".##..",
     "..#..",
     "..#..",
     "..#..",
     "..#..",
     "..#..",
     "....."],

    [".###.",     
     "#...#",
     "....#",
     "..##.",
     ".#...",
     "#....",
     "#####",
     "....."],

    ["#####",
     "....#",
     "....#",
     ".####",
     "....#",
     "....#",
     "#####",
     "....."],
]
NOMBRES = ["1", "2", "3"]

ENTRADA = [".#.#.",
           "....#",
           "..#.#",
           "..##.",
           ".#...",
           "#.#..",
           "#####",
           "#.#.#"]

def matriz_a_vector(filas):
    vector = []
    for i in range(M):
        for j in range(N):
            if filas[i][j] == "#":
                vector.append(1)
            else:
                vector.append(-1)
    return vector


def vector_a_matriz(vector):
    filas = []
    k = 0
    for i in range(M):
        fila = ""
        for j in range(N):
            if vector[k] == 1:
                fila += "#"
            else:
                fila += "."
            k += 1
        filas.append(fila)
    return filas


def imprimir_matriz(filas, titulo):
    print(titulo)
    for fila in filas:
        linea = ""
        for c in fila:
            if c == "#":
                linea += "██"
            else:
                linea += "· "
        print("  " + linea)
    print()


def calcular_pesos(patrones, n):
    T = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        T.append(fila)

    for patron in patrones:
        for i in range(n):
            for j in range(n):
                if i != j:
                    T[i][j] += patron[i] * patron[j]
    return T


def escalon(x, anterior):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return anterior


def recuperar(A, T, n, max_iter=100):
    U = A[:]
    t = 0
    while t < max_iter:
        nuevo = []
        for j in range(n):
            suma = 0
            for i in range(n):
                suma += U[i] * T[i][j]
            nuevo.append(escalon(suma, U[j]))
        t += 1

        igual = True
        for k in range(n):
            if nuevo[k] != U[k]:
                igual = False

        imprimir_matriz(vector_a_matriz(nuevo), f"U({t})")

        if igual:
            print(f"U({t}) = U({t - 1})  ->  FIN\n")
            break
        U = nuevo
    return U


def identificar(U, patrones, nombres):
    for p in range(len(patrones)):
        coincide = True
        for k in range(len(U)):
            if U[k] != patrones[p][k]:
                coincide = False
        if coincide:
            return nombres[p]
    return None


n = M * N
patrones = []
for p in range(len(FIGURAS)):
    patrones.append(matriz_a_vector(FIGURAS[p]))
    imprimir_matriz(FIGURAS[p], f"Patrón guardado: {NOMBRES[p]}")

T = calcular_pesos(patrones, n)

A = matriz_a_vector(ENTRADA)
imprimir_matriz(ENTRADA, "Figura de entrada U(0)")

salida = recuperar(A, T, n)
imprimir_matriz(vector_a_matriz(salida), "Figura recuperada")

nombre = identificar(salida, patrones, NOMBRES)
if nombre is None:
    print("No coincide con ningún patrón guardado.")
else:
    print(f"Figura reconocida: '{nombre}'")