file = open('./input.txt', 'r')
string = file.read()
lists = string.split("\n\n")

fresh_ranges = lists[0].split()
ingredients = list(map(int, lists[1].split()))
# print(len(fresh_ranges), len(ingredients))
fresh_ingredients = set()

for rr in fresh_ranges:
  r = list(map(int, rr.split("-")))
  ra = range(r[0], r[1]+1)
  
  for index, ingredient in enumerate(ingredients):
    if ingredient in ra:
      fresh_ingredients.add(ingredient)
      continue

print(len(fresh_ingredients))