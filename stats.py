def get_num_words(text):
  split = text.split()
  return len(split)

def count_characters(text):
  characters = {}

  for character in text:
    lowercase_character = character.lower()
    if lowercase_character in characters:
      characters[lowercase_character] += 1
    else:
      characters[lowercase_character] = 1
    
  return characters

def sort_on(items):
  return items["num"]

def sort_characters(characters):
  characters_list = []
  for character in characters:
    characters_list.append({"char": character, "num": characters[character]})
  
  characters_list.sort(reverse=True, key=sort_on)
  
  return characters_list
  
