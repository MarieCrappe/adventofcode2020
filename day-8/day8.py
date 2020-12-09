def execute_instruction(instruction, instruction_number, accumulator):
    operation, argument = instruction.split(" ")
    if operation == "nop":
        return instruction_number + 1, accumulator
    if operation == "acc":
        return instruction_number + 1, accumulator + int(argument)
    if operation == "jmp":
        return instruction_number + int(argument), accumulator


def modify_program(instructions, instruction_number):
    operation, argument = instructions[instruction_number].split(" ")
    if operation == "nop":
        instructions[instruction_number] = instructions[instruction_number].replace("nop", "jmp")
    if operation == "jmp":
        instructions[instruction_number] = instructions[instruction_number].replace("jmp", "nop")
    return instructions


def test_program(instructions):
    executed_instructions = []
    accumulator, instruction_number = 0, 0
    while True:
        if instruction_number > len(instructions) - 1:
            print("Program terminated, accumulator at", accumulator)
            break
        if instruction_number in executed_instructions:
            #print("Infinite loop detected, accumulator at", accumulator)
            break
        else:
            executed_instructions.append(instruction_number)
            instruction_number, accumulator = execute_instruction(instructions[instruction_number],
                                                                  instruction_number, accumulator)
    return


if __name__ == '__main__':
    with open("input.txt") as instructions_file:
        instructions = instructions_file.readlines()
        test_program(instructions)
        for i in range(len(instructions)):
            new_instructions = modify_program(list(instructions), i)
            test_program(new_instructions)