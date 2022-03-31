clan = {

}


def add_member(tag, name, age, level):
    clan[tag] = {
        "Name": name,
        "age": age,
        "level": level
    }
    return clan


def display_clan():
    print(clan)


add_member("Voodoo", "Andre Williams", 26, "Beginner")
display_clan()
