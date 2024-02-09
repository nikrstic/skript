import sys

def print_usage_msg():
    print("Usage: (upper|lower|title) <string>")
    sys.exit(0)

if len(sys.argv) != 3:
    print_usage_msg()

act =sys.argv[1]
s=sys.argv[2]
if act.lower()=="lower":
    print(s.lower())
elif act.lower()=="upper":
    print(s.upper())
elif act.lower()== "title":
    print(s.title())
