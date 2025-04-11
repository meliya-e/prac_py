import sys
import math
from collections import defaultdict

def interpret_program(program):
    # 1. Обработка ввода и подготовка данных
    variables = defaultdict(float)  # Переменные (по умолчанию 0)
    labels = {}                     # Метки с их позициями
    commands = []                   # Список команд для выполнения

    # 1.1 Предобработка текста программы
    for line in program:
        line = line.strip()  # Удаляем лишние пробелы в начале и конце строки
        if not line or line.startswith("Эта программа"):  # Пропускаем пустые строки и комментарии
            continue

        if ":" in line:
            label, _, rest = line.partition(":")
            labels[label.strip()] = len(commands)
            line = rest.strip()

        if line:
            commands.append(line.split())

    if any(cmd[0] in {"ifeq", "ifne", "ifgt", "ifge", "iflt", "ifle"} and cmd[3] not in labels for cmd in commands if len(cmd) == 4):
        return

    #2
    pc = 0
    while pc < len(commands):
        cmd, *args = commands[pc]

        match cmd:
            case "stop":
                break

            case "store":
                value, dest = args
                variables[dest] = float(value) if value.replace('.', '', 1).lstrip('-').isdigit() else 0

            case "add" | "sub" | "mul" | "div":
                src, op, dest = args
                src_val, op_val = variables[src], variables[op]
                variables[dest] = (
                    src_val + op_val if cmd == "add" else
                    src_val - op_val if cmd == "sub" else
                    src_val * op_val if cmd == "mul" else
                    src_val / op_val if op_val != 0 else math.inf
                )

            case "ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle":
                src, op, label = args
                src_val, op_val = variables[src], variables[op]
                condition_met = (
                    src_val == op_val if cmd == "ifeq" else
                    src_val != op_val if cmd == "ifne" else
                    src_val > op_val if cmd == "ifgt" else
                    src_val >= op_val if cmd == "ifge" else
                    src_val < op_val if cmd == "iflt" else
                    src_val <= op_val
                )
                if condition_met:
                    pc = labels[label]
                    continue

            case "out":
                print(variables[args[0]])

        pc += 1

program = sys.stdin.read().strip().split("\n")
interpret_program(program)
