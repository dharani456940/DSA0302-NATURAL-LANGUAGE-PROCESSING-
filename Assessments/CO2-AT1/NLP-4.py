# Finite State Morphological Parser

words = ["writes", "writing", "written"]

print("=" * 120)
print("{:<15}{:<25}{:<20}{:<15}{:<15}".format(
    "Word", "State Transition", "Type", "Root", "Normalized"))
print("=" * 120)

for word in words:

    if word == "writes":
        transition = "Start->write->s->End"
        t = "Regular"

    elif word == "writing":
        transition = "Start->write->ing->End"
        t = "Regular"

    elif word == "written":
        transition = "Start->write->written->End"
        t = "Irregular"

    root = "write"

    print("{:<15}{:<25}{:<20}{:<15}{:<15}".format(
        word, transition, t, root, root))
