def check_string(s):
    if s.endswith("ab"):
        return "Accepted"
    else:
        return "Rejected"

string = input("Enter a string: ")
print(check_string(string))