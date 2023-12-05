from sys import stdin

# Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue

def parse_gameid(l):
  i = 5
  num = 0
  while True:
    if l[i].isdigit():
      num = num * 10 + int(l[i])
    else:
      return num

def parse_games(l, r, g, b):
  pos=l.find(":")+1
  for g in l[pos:].split(";"):
    

def parse(l):
  gameid = parse_gameid(l)


for line in stdin:
