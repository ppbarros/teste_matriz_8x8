import numpy as np


coord = np.array([[56, 8, 24, 56, 16, 16, 0, 0],
                  [126, 2, 10, 4, 10, 8, 16, 32],
                  [66, 62, 2, 14, 4, 4, 12, 8],
                  [254, 130, 6, 4, 28, 8, 24, 16],
                  [21, 1, 1, 1, 1, 1, 1, 1],
                  [126, 4, 6, 8, 8, 24, 16, 16],
                  [254, 4, 4, 12, 8, 8, 8, 8],
                  [2, 92, 100, 8, 8, 8, 12],
                  [255, 134, 12, 24, 48, 96, 192, 128],
                  [255, 134, 4, 28, 24, 48, 96, 192],
                  [16, 30, 18, 2, 7, 2, 2, 2],
                  [62, 34, 2, 6, 2, 2, 2, 2],
                  [62, 2, 2, 2, 14, 2, 2, 2],
                  [30, 50, 6, 4, 6, 56, 8,8],
                  [30, 2, 6, 31, 4, 12, 8, 24],
                  [126, 4, 62, 4, 12, 8, 8, 8],
                  [192, 126, 6, 12, 8, 24, 48, 32],
                  [8, 16, 112, 112, 112, 32, 32, 32],
                  [63, 34, 39, 4, 4, 12, 8, 8],
                  [90, 36, 4, 4, 30, 8, 8, 8],
                  [126, 4, 12, 12, 8, 8, 8, 16]])
print(coord.shape)
matrix = coord
f7 = []
# for c in matrix:
#     c /= 21
#     f7.append(c)
print(matrix)

f0 = []
f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []
f8 = []
f9 = []

c1 = float(input("Primeira Coordenada: "))
c2 = float(input("Segunda Coordenada: "))
c3 = float(input("Terceira Coordenada: "))
c4 = float(input("Quarta Coordenada: "))
c5 = float(input("Quinta Coordenada: "))
c6 = float(input("Sexta Coordenada: "))
c7 = float(input("Sétima Coordenada: "))
c8 = float(input("Oitava Coordenada: "))

distance0 = (((c1 - f0[0])**2)+((c2 - f0[1])**2)+((c3 - f0[2])**2)+((c4 - f0[3])**2)+((c5 - f0[4])**2)+((c6 - f0[5])**2)+((c7 - f0[6])**2)+((c8 - f0[7])**2))**0.5
menor = distance0
num = 0


distance1 = (((c1 - f1[0])**2)+((c2 - f1[1])**2)+((c3 - f1[2])**2)+((c4 - f1[3])**2)+((c5 - f1[4])**2)+((c6 - f1[5])**2)+((c7 - f1[6])**2)+((c8 - f1[7])**2))**0.5
if distance1 < menor:
    menor = distance1
    num = 1


distance2 = (((c1 - f2[0])**2)+((c2 - f2[1])**2)+((c3 - f2[2])**2)+((c4 - f2[3])**2)+((c5 - f2[4])**2)+((c6 - f2[5])**2)+((c7 - f2[6])**2)+((c8 - f2[7])**2))**0.5
if distance2 < menor:
    menor = distance2
    num = 2


distance3 = (((c1 - f3[0])**2)+((c2 - f4[1])**2)+((c3 - f4[2])**2)+((c4 - f4[3])**2)+((c5 - f4[4])**2)+((c6 - f4[5])**2)+((c7 - f4[6])**2)+((c8 - f4[7])**2))**0.5
if distance3 < menor:
    menor = distance3
    num = 3


distance4 = (((c1 - f4[0])**2)+((c2 - f4[1])**2)+((c3 - f4[2])**2)+((c4 - f4[3])**2)+((c5 - f4[4])**2)+((c6 - f4[5])**2)+((c7 - f4[6])**2)+((c8 - f4[7])**2))**0.5
if distance4 < menor:
    menor = distance4
    num = 4


distance5 = (((c1 - f5[0])**2)+((c2 - f5[1])**2)+((c3 - f5[2])**2)+((c4 - f5[3])**2)+((c5 - f5[4])**2)+((c6 - f5[5])**2)+((c7 - f5[6])**2)+((c8 - f5[7])**2))**0.5
if distance5 < menor:
    menor = distance5
    num = 5


distance6 = (((c1 - f6[0])**2)+((c2 - f6[1])**2)+((c3 - f6[2])**2)+((c4 - f6[3])**2)+((c5 - f6[4])**2)+((c6 - f6[5])**2)+((c7 - f6[6])**2)+((c8 - f6[7])**2))**0.5
if distance6 < menor:
    menor = distance6
    num = 6


distance7 = (((c1 - f7[0])**2)+((c2 - f7[1])**2)+((c3 - f7[2])**2)+((c4 - f7[3])**2)+((c5 - f7[4])**2)+((c6 - f7[5])**2)+((c7 - f7[6])**2)+((c8 - f7[7])**2))**0.5
if distance7 < menor:
    menor = distance7
    num = 7


distance8 = (((c1 - f8[0])**2)+((c2 - f8[1])**2)+((c3 - f8[2])**2)+((c4 - f8[3])**2)+((c5 - f8[4])**2)+((c6 - f8[5])**2)+((c7 - f8[6])**2)+((c8 - f8[7])**2))**0.5
if distance8 < menor:
    menor = distance8
    num = 8


distance9 = (((c1 - f9[0])**2)+((c2 - f9[1])**2)+((c3 - f9[2])**2)+((c4 - f9[3])**2)+((c5 - f9[4])**2)+((c6 - f9[5])**2)+((c7 - f9[6])**2)+((c8 - f9[7])**2))**0.5
if distance9 < menor:
    num = 9



print(f'É mais provável que este seja o algarismo {num}')
