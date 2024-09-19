# Пункты задачи:
# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
# Создайте внутри функции пустой список same_words, который пополнится нужными словами.
# При помощи цикла for переберите предполагаемо подходящие слова.
# Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# После цикла верните образованный функцией список same_words.
# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.


def single_root_words(root_word: str, *other_words) -> list[str]:
    same_words = []

    for word in other_words:
        if root_word in word or word in root_word:
            same_words += [word]

    return same_words


print(single_root_words('кошкательник', 'котенок', 'котейка', 'кошка', 'котопес'))