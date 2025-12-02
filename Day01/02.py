import math

file = open('./input.txt', 'r')
string = file.read()
lines = string.split("\n")

result = 0
dial = 50
for line in lines:
  dir = line[0]
  nr = int(line[1:])
  if dial == 0:
    result -= 1

  if dir == 'L':
    dial -= nr
  else:
    dial += nr
  
  new_dial = dial % 100
  # print("DIAL", new_dial)
  
  if dial > 99 or dial < 0:
    # print("rotated over 0:", dir, nr, dial, abs(math.floor(dial/100)))
    r = abs(math.floor(dial / 100))
    # if new_dial == 0:
    #   r -= 1
    # print(r)
    result += r

  dial = new_dial
  if dial == 0:
    result += 1
  # dial = dial % 100
  # print("DIAL", dial)
  # if dial == 0:
  #   result += 1

print(result)

# more bruteforce style
dial = 50
result = 0
for line in lines:
  dir = line[0]
  nr = int(line[1:])
  for i in range(nr):
    if dir == 'L':
      dial -= 1
    else:
      dial += 1
    
    dial = dial % 100
    if dial == 0:
      result += 1

print(result)