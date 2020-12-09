def find_invalid_number(puzzle, preamble):
    for i in range(preamble, len(puzzle)):
        found_sum = False
        target = puzzle[i]
        for j in range(i - preamble, i):
            to_find = target - puzzle[j]
            for k in range(j + 1, i):
                if puzzle[k] != puzzle[j] and puzzle[k] == to_find:
                    found_sum = True
                    break
            if found_sum:
                break
        if not found_sum:
            return i, target


def find_encryption_weakness(puzzle, target):
    for i in range(len(puzzle)):
        contiguous_sum = puzzle[i]
        for j in range(i+1, len(puzzle)):
            contiguous_sum += puzzle[j]
            if contiguous_sum == target:
                return min(puzzle[i:j+1]) + max(puzzle[i:j+1])
            if contiguous_sum > target:
                break

if __name__ == '__main__':
    preamble = 25
    half_preamble = preamble/2

    with open("input.txt") as puzzle_file:
        puzzle = puzzle_file.readlines()

        for number in range(len(puzzle)):
            puzzle[number] = int(puzzle[number])

        position, target = find_invalid_number(puzzle, preamble)
        encryption_weakness = find_encryption_weakness(puzzle, target)
        print(target, encryption_weakness)