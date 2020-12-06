if __name__ == '__main__':
    with open("input.txt") as answers_file:
        groups = answers_file.read().split('\n\n')
        first_solution = 0
        second_solution = 0
        for group in groups:
            group_answers = group.split('\n')
            first_solution += len("".join(set(''.join(group_answers))))
            common_answers = set.intersection(*(set(line) for line in group_answers))
            second_solution += len(common_answers)
        print(first_solution, second_solution)