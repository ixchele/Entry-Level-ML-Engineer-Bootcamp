import sys

arg = sys.argv[1]
print("AssertionError: more than one argument is provided" if len(sys.argv) != 2
      else "AssertionError: argument is not an integer" if not arg.isdigit()
      else "I'm Zero." if int(arg) == 0
      else "I'm Even." if int(arg)%2 == 0
      else "I'm Odd.")

