# Morphological Parsing

words = ["unhappy", "happiness", "happily"]

print("=" * 110)
print("{:<15}{:<12}{:<12}{:<12}{:<18}{:<15}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))
print("=" * 110)

for word in words:

    if word == "unhappy":
        prefix = "un"
        root = "happy"
        suffix = "-"
        t = "Derivational"

    elif word == "happiness":
        prefix = "-"
        root = "happy"
        suffix = "ness"
        t = "Derivational"

    elif word == "happily":
        prefix = "-"
        root = "happy"
        suffix = "ly"
        t = "Derivational"

    print("{:<15}{:<12}{:<12}{:<12}{:<18}{:<15}".format(
        word, prefix, root, suffix, t, root))
