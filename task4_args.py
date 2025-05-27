import argparse

parser = argparse.ArgumentParser(description="Скрипт с аргументами и флагами")
parser.add_argument("number", type=int, help="Число")
parser.add_argument("text", type=str, help="Строка")
parser.add_argument("--verbose", action="store_true", help="Вывод дополнительной информации")
parser.add_argument("--repeat", type=int, default=1, help="Количество повторов строки")

args = parser.parse_args()

if args.verbose:
    print(f"[VERBOSE] Получено число: {args.number}")
    print(f"[VERBOSE] Повтор строки: {args.repeat}")

for _ in range(args.repeat):
    print(args.text)
