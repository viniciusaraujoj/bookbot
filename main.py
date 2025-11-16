import sys

from stats import get_num_words, count_characters, sort_characters

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path = sys.argv[1]
  text = get_book_text(path)
  words_count = get_num_words(text)
  char_count = count_characters(text)
  sorteded_chars = sort_characters(char_count)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {words_count} total words")
  print("--------- Character Count -------")
  for char in sorteded_chars:
    if not char["char"].isalpha():
      continue

    print(f"{char["char"]}: {char["num"]}")
  print("============= END ===============")
  

def get_book_text(filepath):
  with open(filepath) as f:
    text_content = f.read()
    return text_content


  
main()
