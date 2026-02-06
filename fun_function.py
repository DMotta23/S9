def bond_greet(name):
    """
    Returns the bond greet:
    :param name: the name to use
    :return: string
    """
    return f"The name is {name}"

def create_bond_name(first_name, last_name = "Bond"):
    """
    Returns: last_name, first_name last_name
    :param first_name:
    :param last_name:
    :return:
    """
    return f"{last_name}, {first_name} {last_name}"

print(bond_greet(create_bond_name("Campbell", "Epstein")))