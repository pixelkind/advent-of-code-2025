file = open('./input.txt', 'r')
string = file.read()
ranges = string.split(",")

result = 0
for r in ranges:
  data = list(map(int, r.split("-")))
  for i in range(data[0], data[1]+1):
    s = str(i)
    length = len(s)
    check_length = int(length / 2)
    for x in range(check_length):
      if length % (x+1) == 0:
        if s.count(s[0:(x+1)]) == int(length / (x + 1)):
          # print("Found:", i, x+1, s[0:(x+1)], int(length / (x + 1)))
          result += i
          break

print(result)