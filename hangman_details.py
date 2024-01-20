

word_list = ['Eclipse', 'Velvet', 'Elephant', 'Necklace', 'Jigsaw', 'Kindle', 'Glitter', 'Adventure', 'Sandwich', 'Delicate', 'Aquarium', 'Nectar', 'Velocity', 'Dog', 'Tornado', 'Banana', 'Fantasy', 'Cherish', 'Monopoly', 'Whistle', 'Penguin', 'Vanilla', 'Peppermint', 'Apple', 'Lighthouse', 'Mountain', 'Umbrella', 'Bliss', 'Kite', 'Dazzle', 'Oasis', 'Sunshine', 'Guitar', 'Cascade', 'Panorama', 'Telescope', 'Vivid', 'Kaleidoscope', 'Blissful', 'Forest', 'Harmony', 'Serenity', 'Octopus', 'Chocolate', 'Tranquility', 'Quilt', 'Infinity', 'Luminous', 'Koala', 'Vibrant', 'Radiant', 'Lemonade', 'Feather', 'Dream', 'Galaxy', 'Lavender', 'Tranquil', 'Jellybean', 'Happiness', 'Nutmeg', 'Nostalgia', 'Carnival', 'Car', 'Utopia', 'Butterfly', 'Rainbow', 'Yellow', 'Gondola', 'Moonlight', 'Radiance']

stages = ['''
+---+
|   |   
|   O   
|  /|\  
|  / \  
|       
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import os, time
os.system("clear")

win = ["finalwin1.txt", "finalwin2.txt"]
lost = ["finallost1.txt", "finallost3.txt"]

def animator(filename, delay=1, repeat=20):
    frames = []
    for name in filename:
        with open(name, "r", encoding="utf-8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
          print("".join(frame))
          time.sleep(delay)
          os.system("clear")

def animator2(filename, delay=1, repeat=20):
    frames = []
    for name in filename:
        with open(name, "r", encoding="utf-8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
          print("".join(frame))
          time.sleep(delay)
          os.system("clear")
    with open("finallost2.txt") as final:
      content = final.readlines()
      print("".join(content))


if __name__ == '__main__':
    animator(win, delay=0.1, repeat=10)
    animator2(lost, delay=0.5, repeat=5)
