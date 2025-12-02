file = open('./input.txt', 'r')
string = file.read()
ranges = string.split(",")

result = 0
for r in ranges:
  data = list(map(int, r.split("-")))
  for i in range(data[0], data[1]+1):
    s = str(i)
    if len(s) % 2 == 0:
      h = int(len(s) / 2)
      l = s[:h]
      r = s[h:]
      if l == r:
        # print("Found:", i)
        result += i

print(result)