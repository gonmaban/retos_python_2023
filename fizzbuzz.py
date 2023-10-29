'''
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */'''
#!/usr/bin/env python
# -*- coding: utf_8 -*-

for i in range(100):
    valor = i+1
    if valor%15 == 0:
        valor = 'fizzbuzz'
    elif valor%3 == 0:
        valor = 'fizz'
    elif valor%5 == 0:
        valor = 'buzz'

    print(valor)
