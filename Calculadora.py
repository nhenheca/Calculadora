prioridade = ["*", "/", "+", "-"]

conta = "22-5*3/1+10"

mk1 = conta.find('(') + 1
mk2 = conta.find(')', mk1)
subString = conta[mk1:mk2]


def getNumberBack(index, array):
  aux = 0
  while aux == 0:
    if (array[index - 1].isnumeric()):
      index = index - 1
    else:
      aux = 1
      if (index < 0):
        index = 0
      return index


def getNumberFront(index, array):
  aux = 0
  while aux == 0:
    if (index == len(array) - 1):
      return index

    if (array[index + 1].isnumeric()):
      index = index + 1
    else:
      aux = 1
      if (index > len(array)):
        index = len(array)
      return index


def operate(operator, n1, n2):
  if (operator == "*"):
    return n1 * n2

  if (operator == "/"):
    return n1 // n2

  if (operator == "+"):
    return n1 + n2

  if (operator == "-"):
    return n1 - n2


def calcular(conta):
  try:
    aux = 0
    isDone = 0

    while isDone == 0:
      if (conta.find(prioridade[aux]) != -1):
        index = conta.find(prioridade[aux])

        backIndex = getNumberBack(index, conta)
        frontIndex = getNumberFront(index, conta)

        n1slice = slice(backIndex, index)
        n2slice = slice(index + 1, frontIndex + 1)
        operationslice = slice(backIndex, frontIndex + 1)

        n1 = conta[n1slice]
        n2 = conta[n2slice]
        operation = conta[operationslice]

        res = operate(conta[index], int(n1), int(n2))

        conta = conta.replace(operation, str(res))
        print(conta)
      else:
        aux = aux + 1

      if (aux == 4):
        isDone = 1
        return conta
  except:
    print("Formatação Inválida")


print('Introduza a conta:')
conta = input()
calcular(conta)
