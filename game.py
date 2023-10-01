import random

words = ["function", "decorator", "iterator"]
word = random.choice(words)

attempts = 10
chars = ""
calls = 0


def profiler(func):
    # декоратор, позволяющий проверять была ли попытка игры провальной
    def wrapped(*args, **kwargs):
        attempt = int(func(*args, **kwargs))
        if attempt == 1:
            print(f"You have {attempts - calls - 1} more guesses")
        return attempt

    return wrapped


@profiler
def game_step(letter, letters):
    # возвращается булев тив в зависимости угадана буква или нет
    if letter in word:
        print("".join([char if char in letters else "_" for char in word]),
              f"guess a character: {letter}")
        return False
    else:
        print("Wrong")
        return True


def is_win(letters, word):
    # возвращает булев тип, в зависимости угаданы все буквы или нет
    for char in word:
        if char not in letters:
            return False
    return True


print("Start guessing...")


def input_char():
    # проверяет, введена ли одна буква
    while True:
        input_str = input()
        if len(input_str) == 1:
            return input_str
        else:
            print('Input letter')


while True:
    if is_win(chars, word):
        print(f"{word} You won")
        break
    char = input_char()
    chars += char
    calls += int(game_step(char, chars))
    if calls > 10:
        print("game over")
        break
