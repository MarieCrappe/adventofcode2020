def check_containing_bags(checked_bags, can_be_contained_by, color):
    if color not in can_be_contained_by:
        return
    for bag in can_be_contained_by[color]:
        if bag not in checked_bags:
            checked_bags.append(bag)
            check_containing_bags(checked_bags, can_be_contained_by, bag)
    return


def build_affiliation_graph(bags_rules):
    can_be_contained_by = dict()

    for bag_rule in bags_rules:
        if bag_rule.find("no other bags") != -1:
            continue
        initial_color = bag_rule.split(" bags contain ")[0]

        for contained_bag in bag_rule.split(" bags contain ")[1].split(", "):
            color = contained_bag[2:].replace(" bags", "").replace(" bag", "").replace(".\n", "")
            if color not in can_be_contained_by:
                can_be_contained_by[color] = [initial_color]
            else:
                can_be_contained_by[color].append(initial_color)
    return  can_be_contained_by


def build_dependency_graph(bags_rules):
    bag_contains = dict()

    for bag_rule in bags_rules:
        if bag_rule.find("no other bags") != -1:
            continue
        initial_color = bag_rule.split(" bags contain ")[0]

        for bag in bag_rule.split(" bags contain ")[1].split(", "):
            number = bag[0]
            color = bag[2:].replace(" bags", "").replace(" bag", "").replace(".\n", "")
            if initial_color not in bag_contains:
                bag_contains[initial_color] = {color: int(number)}
            else:
                bag_contains[initial_color][color] = int(number)
    return bag_contains


def count_containing_bags(can_be_contained_by, color):
    checked_bags = []
    check_containing_bags(checked_bags, can_be_contained_by, color)
    return len(checked_bags)

def count_contained_bags(bags_contain, color):
    if color not in bags_contain:
        return 0
    contained_bags = 0
    for bag, n in bags_contain[color].items():
        contained_bags += n + n * count_contained_bags(bags_contain, bag)
    return contained_bags


if __name__ == '__main__':
    with open("input.txt") as bags_rules_file:
        bags_rules = bags_rules_file.readlines()
        can_be_contained_by = build_affiliation_graph(bags_rules)
        print(count_containing_bags(can_be_contained_by, "shiny gold"))
        bags_contain = build_dependency_graph(bags_rules)
        print(count_contained_bags(bags_contain, "shiny gold"))