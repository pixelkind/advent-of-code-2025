file = open('./input.txt', 'r')
string = file.read()
banks = string.split("\n")

result = 0

for bank in banks:
  b = list(map(int, list(bank)))
  first = max(b[:-1])
  index = b.index(first)
  second = max(b[index+1:])
  result += int(str(first) + str(second))

print(result)