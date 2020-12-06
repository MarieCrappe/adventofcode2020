if __name__ == '__main__':
    with open("input.txt") as answers_file:
        groups = answers_file.read().split('\n\n')
        first_answer = 0
        second_answer = 0
        for group in groups:
            group_answers = ''.join(group.split('\n'))
            first_answer += len("".join(set(group_answers)))
            common_answers = set(group.split('\n')[0])
            for answer in group.split('\n'):
                common_answers = common_answers.intersection(set(answer))
            second_answer += len(common_answers)
        print(first_answer, second_answer)
