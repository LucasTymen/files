#close_this_file = open('fun_file.txt') <<== old syntax
with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)
