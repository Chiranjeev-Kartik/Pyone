def remove_common(str_1, str_2):
    # Returns the number of uncommon elements.
    common = set(str_1).intersection(set(str_2))
    list_1, list_2 = [x for x in str_1], [x for x in str_2]
    for x in common:
        list_1.remove(x), list_2.remove(x)
    return len(list_1) + len(list_2)


def count_flames(count):
    # Based on uncommon elements, Returns a relation.
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(flames) > 1:
        flames.pop(count % len(flames) - 1)
    return flames[0]


name_1, name_2 = input('Enter Name 1: ').lower(), input('Enter Name 2: ').lower()
print(f'Relationship: {count_flames(remove_common(name_1, name_2))}')
