file = open('./input.txt', 'r')
string = file.read()
papers = list(map(list, string.split("\n")))

def check_field(x, y, papers):
  if y < 0 or y >= len(papers) or x < 0 or x >= len(papers[0]):
    return False 
  return papers[y][x] == '@'

result = 0

def update_papers(papers):
  global result
  new_papers = list([r.copy() for r in papers.copy()])
  changes = False

  for y, row in enumerate(papers):
    for x, field in enumerate(row):
      if field == '.':
        continue
      
      count = 0
      for xx in range(-1, 2):
        for yy in range(-1, 2):
          if check_field(x + xx, y + yy, papers):
            count += 1
      
      if count <= 4:
        new_papers[y][x] = '.'
        changes = True
        result += 1
  
  print(result, changes)
  if changes:
    update_papers(new_papers)

update_papers(papers)
print(result)