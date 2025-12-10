file = open('./input.txt', 'r')
string = file.read()
lines = string.split("\n")
matrix = list([list(filter(None, line.split(" "))) for line in lines])

operators = matrix.pop()

matrix = [list(map(int, line)) for line in matrix]

result = 0
for index, operator in enumerate(operators):
  r = 0
  for row in matrix:
    value = row[index]
    if operator == '+':
      r += value
    elif operator == '-':
      r -= value
    elif operator == '*':
      if r == 0:
        r = value
      else:
        r *= value
    else:
      if r == 0:
        r = value
      else:
        r /= value
  result += r

print(result)
  