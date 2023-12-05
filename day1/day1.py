from sys import stdin

first_run = True


digits = [
  "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

def find_digit(line, d):
  return (line.find(d), line.rfind(d))


first, last = 0,0
p_first, p_last = 10**5, -1
arr=[]
for line in stdin:
  print(line)
  for i in range(len(digits)):
    f, l = find_digit(line, digits[i])
    if f < p_first and f!=-1:
      print(f)
      p_first = f
      first = i+1
    if l > p_last and l!=-1:
      p_last = l
      last = i+1

  for i in range(len(line)):
    if line[i].isdigit():
      if i < p_first:
        p_first = i
        first = int(line[i])
      if i > p_last:
        p_last = i
        last = int(line[i])

  # print(first+last)
  arr.append(str(first)+str(last))
  print(arr)
  first, last = 0, 0
  p_first, p_last = 10**5, -1
acc = 0
for i in arr:
  acc+=int(i)
print(acc)