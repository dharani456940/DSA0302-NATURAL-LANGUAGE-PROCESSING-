# Porter Stemmer (Simple Demonstration)

words = ["relational", "relation", "relate"]

print("=" * 120)
print("{:<15}{:<30}{:<20}{:<15}".format(
    "Word", "Applied Rule", "Intermediate", "Final Stem"))
print("=" * 120)

for word in words:

    if word == "relational":
        rule = "Remove 'ational'"
        intermediate = "relate"
        stem = "relat"

    elif word == "relation":
        rule = "Remove 'ion'"
        intermediate = "relate"
        stem = "relat"

    elif word == "relate":
        rule = "Remove final 'e'"
        intermediate = "relat"
        stem = "relat"

    print("{:<15}{:<30}{:<20}{:<15}".format(
        word, rule, intermediate, stem))
