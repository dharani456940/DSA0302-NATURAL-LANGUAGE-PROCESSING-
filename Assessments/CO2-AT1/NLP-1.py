# Morphological Analysis Pipeline

words = ["connected", "connecting", "connection"]

print("=" * 90)
print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
print("=" * 90)

for word in words:
    if word.endswith("ed"):
        root = "connect"
        suffix = "ed"
        t = "Inflectional"
    elif word.endswith("ing"):
        root = "connect"
        suffix = "ing"
        t = "Inflectional"
    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        t = "Derivational"
    else:
        root = word
        suffix = "-"
        t = "None"

    print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
        word, root, suffix, t, root))
