# Stemming Based Preprocessing

words = ["played", "player", "playing"]

print("=" * 110)
print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
    "Word", "Stem", "Affix Removed", "Type", "Normalized"))
print("=" * 110)

for word in words:

    if word.endswith("ed"):
        stem = "play"
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        stem = "play"
        affix = "ing"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = "play"
        affix = "er"
        t = "Derivational"

    print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
        word, stem, affix, t, stem))
