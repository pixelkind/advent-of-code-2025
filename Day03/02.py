file = open('./input.txt', 'r')
string = file.read()
banks = string.split("\n")

result = 0

for bank in banks:
  b = list(map(int, list(bank)))
  numbers = []

  prev_index = 0
  for i in range(12):
    max_index = len(b) - (11 - i)
    number = max(b[prev_index:max_index])
    numbers.append(number)
    prev_index = b.index(number, prev_index) + 1

  result += int("".join(map(str, numbers)))

print(result)