file = open('./input.txt', 'r')
string = file.read()
lists = string.split("\n\n")

fresh_ranges = lists[0].split()
final_ranges = []
fresh_ingredients = []

fresh_ranges = [list(map(int, rr.split("-"))) for rr in fresh_ranges]
fresh_ranges.sort()

for rr in fresh_ranges:
  r = rr
  start = r[0]
  stop = r[1]
  start_within = False
  stop_within = False
  start_index = -1
  stop_index = -1

  for index, fr in enumerate(final_ranges):
    if fr[0] <= start <= fr[1]:
      print("start within", index, start, fr[0], fr[1])
      start_within = True
      start_index = index
    if fr[0] <= stop <= fr[1]:
      print("stop within", index, stop, fr[0], fr[1])
      stop_within = True
      stop_index = index
    

  if not start_within and not stop_within:
    final_ranges.append([start, stop])
  elif start_within and not stop_within:
    final_ranges[start_index][1] = stop
  elif stop_within and not start_within:
    final_ranges[stop_index][0] = start
  elif start_index == stop_index and start_index != -1:
    pass
  else:
    final_ranges[start_index][1] = final_ranges[stop_index][1]
    del final_ranges[stop_index]
  
  print("-----", len(final_ranges))
  # print(final_ranges)
  
result = 0
for r in final_ranges:
  result += r[1] - r[0] + 1

print(result)
