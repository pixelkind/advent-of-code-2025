file = open('./input.txt', 'r')
string = file.read()
lines = string.split("\n")

result = 0
dial = 50
for line in lines:
  dir = line[0]
  nr = int(line[1:])
  if dir == 'L':
    dial -= nr
  else:
    dial += nr
  
  dial = dial % 100
  if dial == 0:
    result += 1

print(result)