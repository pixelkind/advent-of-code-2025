
file = open('./input.txt', 'r')
string = file.read()
lines = string.split("\n")
operators = lines.pop()

# print(lines, operators)

result = 0
current_operator = ''
r = 0
for index, operator in enumerate(operators):
  if operator.strip():
    current_operator = operator
    result += r
    r = 0

  value = ''
  for row in lines:
    value += row[index]

  if value.strip():
    # print(value, int(value))
    if current_operator == '+':
      r += int(value)
    elif current_operator == '*':
      if r == 0:
        r = int(value)
      else:
        r *= int(value)
  

result += r
print(result)
