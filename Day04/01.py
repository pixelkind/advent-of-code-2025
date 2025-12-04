file = open('./input.txt', 'r')
string = file.read()
papers = list(map(list, string.split("\n")))

def check_field(x, y):
  if y < 0 or y >= len(papers) or x < 0 or x >= len(papers[0]):
    return False 
  return papers[y][x] == '@'

result = 0
for y, row in enumerate(papers):
  for x, field in enumerate(row):
    if field == '.':
      continue
    
    count = 0
    for xx in range(-1, 2):
      for yy in range(-1, 2):
        if check_field(x + xx, y + yy):
          count += 1
    
    if count <= 4:
      result += 1

print(result)