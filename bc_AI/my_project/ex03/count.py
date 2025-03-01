import sys
import string

def text_analyzer(text):
    up_count   = sum(1 for c in text if c.isupper())
    lo_count   = sum(1 for c in text if c.islower())
    punc_count = sum(1 for c in text if c in string.punctuation)
    sp_count   = sum(1 for c in text if c == ' ')

    print(f"The text contains {len(text)} printable character(s):\n"
    f"- {up_count} upper letter(s)\n"
    f"- {lo_count} lower letter(s)\n"
    f"- {punc_count} punctuation mark(s)\n"
    f"- {sp_count} space(s)")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    elif len(sys.argv) == 1:
        print("")
    else:
        text_analyzer(sys.argv[1])
