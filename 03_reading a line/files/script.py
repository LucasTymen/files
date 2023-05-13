with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
  second_line = first_line_doc.readline()
  print(first_line)
  print(second_line)
