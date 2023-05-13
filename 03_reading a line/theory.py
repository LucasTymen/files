"""

Learn Python: Files
Reading a Line

Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, .readline(), which
will only read a single line at a time. If the entire document is read line by line in this way subsequent calls
to .readline() will not throw an error but will start returning an empty string (""). Suppose we had this file:

millay_sonnet.txt

I shall forget you presently, my dear,
So make the most of this, your little day,
Your little month, your little half a year,
Ere I forget, or die, or move away,

script.py
"""
with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)
"""
This script also creates a file object called sonnet_doc that points to the file millay_sonnet.txt. It then reads in the
first line using sonnet_doc.readline() and saves that to the variable first_line. It then saves the second line (So make
the most of this, your little day,) into the variable second_line and then prints it out.
Instructions
1.

Using a with statement, create a file object pointing to the file just_the_first.txt. Store that file object in the
variable first_line_doc.

Remember to open a file using with syntax:
"""
with open('filename.txt') as file_object:
    print()
  # indented block here
"""
2.

Save the first line of just_the_first.txt into the variable first_line.

Use the file object method .readline() to store a line into the variable line.
3.

Print out the variable first_line.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    I accidently used .readlines(), but why does it look different than in the last exercise?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
