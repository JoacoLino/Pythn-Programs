"""""
FizzBuzz

 * Escribe un programa que muestre por consola (con un print)
 *  (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""


def fizzbuzz(n):
    answer = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0 :
            answer.append("fizzbuzz")
        elif i % 3==0:
            answer.append("fizz")
        elif i % 5 == 0:
            answer.append("buzz")
        else:
            answer.append(i)