a = [[3, 5, 1],
     [8, 6, 2]]
b = [[-1, 7, 9],
     [2, -5, 3]]


# for x in range(0, 2):
#     for n in range(0, 3):
#         pos = a[x][n]
#         print(
#             f"fila A: nºfila {[x+1]} nº columna {[n+1]} se encuentra el elemento: {pos}")

for x in range(0, 2):
    for n in range(0, 3):
        elemento_pos = a[x][n]
        if (elemento_pos == a[0][0]):
            print(
                f"fila A: nºfila {x+1} nº columna {n+1} se encuentra el elemento: {elemento_pos}")
        elif (elemento_pos == a[0][1]):
            print(
                f"fila A: nºfila {x+1} nº columna {n+1} se encuentra el elemento: {elemento_pos}")
        elif (elemento_pos == a[1][0]):
            print(
                f"fila A: nºfila {x+1} nº columna {n+1} se encuentra el elemento: {elemento_pos}")
        elif (elemento_pos == a[1][1]):
            print(
                f"fila A: nºfila {x+1} nº columna {n+1} se encuentra el elemento: {elemento_pos}")


print()


# for i in range(0, 2):
#     for p in range(0, 3):
#         pos = b[i][p]
#         print(
#             f"fila B: nºfila {[i+1]}, nº columna {[p+1]} se encuentra el elemento: {pos}")


c = [[0, 0, 0], [0, 0, 0]]

print()

for r in range(0, 2):
    for f in range(0, 3):
        matrizA = a[r][f]
        matrizB = b[r][f]
        suma = matrizA + matrizB
        if (c[r][f] == 0):
            c[r][f] = suma

print(f"Suma de C (matriz A + matriz B) = {c}")
print()

d = [[0, 0, 0], [0, 0, 0]]


for q in range(0, 2):
    for t in range(0, 3):
        matriz_A = a[q][t]
        matriz_B = b[q][t]
        resta = matriz_A - matriz_B
        if (d[q][t] == 0):
            d[q][t] = resta

print(f"Resta de D (matriz A - matriz B) = {d}")

print()


e = [[0, 0, 0], [0, 0, 0]]

for y in range(0, 2):
    for r in range(0, 3):
        matriz_b = b[y][r]
        matriz_a = a[y][r]
        resta_B_A = matriz_b - matriz_a
        if (e[y][r] == 0):
            e[y][r] = resta_B_A

print(f"Resta de E (matriz B - matriz A) = {e}")

print()


# a = [[3, 5, 1],
#      [8, 6, 2]]
# b = [[-1, 7, 9],
#      [2, -5, 3]]

A_t = [[0, 0],
       [0, 0],
       [0, 0]]

B_t = [[0, 0],
       [0, 0],
       [0, 0]]

C_t = [[0, 0],
       [0, 0],
       [0, 0]]

D_t = [[0, 0],
       [0, 0],
       [0, 0]]

E_t = [[0, 0],
       [0, 0],
       [0, 0]]
# for k in range(0, 2):
#     for l in range(0, 3):
#         if (a[k][l] == a[0][l]):
#             at = a[k][l]
#             if (A_t[t][0] == 0):
#                 A_t[t][0] = at

# print(A_t)

acumu = 0
while acumu <= 2:
    if (A_t[acumu][0] == 0):
        A_t[acumu][0] = a[0][acumu]

    if (A_t[acumu][1] == 0):
        A_t[acumu][1] = a[1][acumu]

    if (B_t[acumu][0] == 0):
        B_t[acumu][0] = b[0][acumu]

    if (B_t[acumu][1] == 0):
        B_t[acumu][1] = b[1][acumu]

    if (C_t[acumu][0] == 0):
        C_t[acumu][0] = c[0][acumu]

    if (C_t[acumu][1] == 0):
        C_t[acumu][1] = c[1][acumu]

    if (D_t[acumu][0] == 0):
        D_t[acumu][0] = d[0][acumu]

    if (D_t[acumu][1] == 0):
        D_t[acumu][1] = d[1][acumu]

    if (E_t[acumu][0] == 0):
        E_t[acumu][0] = e[0][acumu]

    if (E_t[acumu][1] == 0):
        E_t[acumu][1] = e[1][acumu]

    acumu = acumu + 1


print(
    f"\n\nMatriz At: {A_t}\nMatriz Bt: {B_t}\nMatriz Ct: {C_t}\nMatriz Dt: {D_t}\nMatriz Et: {E_t}")


def escalar_5_A_B_C_D_E_masAtBtCtDtEt():
    # Matriz A
    for x in range(0, 2):
        for n in range(0, 3):
            escalarmatrizA = a[x][n] * -5
            a[x][n] = escalarmatrizA

            escalarmatrizB = b[x][n] * -5
            b[x][n] = escalarmatrizB

            escalarmatrizC = c[x][n] * -5
            c[x][n] = escalarmatrizC

            escalarmatrizD = d[x][n] * -5
            d[x][n] = escalarmatrizD

            escalarmatrizE = e[x][n] * -5
            e[x][n] = escalarmatrizE

    print(
        f"\nMatriz A escalar * -5: {a}\nMatriz B escalar * -5: {b}\nMatriz C escalar * -5: {c}\nMatriz D escalar * -5: {d}\nMatriz E escalar * -5: {e}\n")

    for r in range(0, 3):
        for p in range(0, 2):
            escalarMatrizAt = A_t[r][p] * -5
            A_t[r][p] = escalarMatrizAt

            escalarMatrizBt = B_t[r][p] * -5
            B_t[r][p] = escalarMatrizBt

            escalarMatrizCt = C_t[r][p] * -5
            C_t[r][p] = escalarMatrizCt

            escalarMatrizDt = D_t[r][p] * -5
            D_t[r][p] = escalarMatrizDt

            escalarMatrizEt = E_t[r][p] * -5
            E_t[r][p] = escalarMatrizEt

    print(
        f"\nMatriz At escalar * -5: {A_t}\nMatriz Bt escalar * -5: {B_t}\nMatriz Ct escalar * -5: {C_t}\nMatriz Dt escalar * -5: {D_t}\nMatriz Et escalar * -5: {E_t}")


escalar_5_A_B_C_D_E_masAtBtCtDtEt()
