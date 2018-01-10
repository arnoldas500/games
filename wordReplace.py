def censor(text, word):
  print text.split()
  num = len(word)
  ass = "*" * num
  lists = text.split()
  for i, w in enumerate(lists):
    if w == word:
      lists[i] = ass
      print lists
  #print " ".join()
  return " ".join(lists)
