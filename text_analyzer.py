from collections import Counter

text = input("Enter a text that u want to see: ").strip()

if not text:
    print("Ви нічого не ввели!")
else:
    # Основні підрахунки
    total_chars = len(text)  # з пробілами
    chars_without_spaces = len(text.replace(" ", ""))  # без пробілів
    words_list = text.split()  # список слів
    number_of_words = len(words_list)

    # Підрахунок речень (простий спосіб)
    sentences = text.replace("!", ".").replace("?", ".").split(".")
    sentences = [s.strip() for s in sentences if s.strip()]
    sentences_count = len(sentences)

    # Топ 5 найдовших слів
    longest_words = sorted(set(words_list), key=len, reverse=True)
    top_5_longest = longest_words[:5]

    # Підрахунок регістру
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    total_letters = upper_count + lower_count

    # Найчастіше слово
    words_lower = text.lower().split()
    if words_lower:
        word_counts = Counter(words_lower)
        most_common_word = word_counts.most_common(1)[0]


        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТИ АНАЛІЗУ")
        print("=" * 50)
        print(f"Кількість символів (з пробілами) : {total_chars}")
        print(f"Кількість символів (без пробілів): {chars_without_spaces}")
        print(f"Кількість слів                  : {number_of_words}")
        print(f"Кількість речень                : {sentences_count}")
        print(f"Найчастіше слово                : '{most_common_word[0]}' "
              f"({most_common_word[1]} разів)")
        print(f"ТОП-5 НАЙДОВШИХ СЛІВ:")
        for i, word in enumerate(top_5_longest, 1):
            print(f"{i}. '{word}' - {len(word)} символів")
        print("\n=== СТАТИСТИКА ПО РЕГІСТРУ ===")
        print(f"Великих літер  (A-Z): {upper_count}")
        print(f"Малих літер    (a-z): {lower_count}")
        print(f"Всього літер         : {total_letters}")
        if total_letters > 0:
            print(f"Відсоток великих літер: {upper_count / total_letters * 100:.1f}%")
            print(f"Відсоток малих літер  : {lower_count / total_letters * 100:.1f}%")
        print("=" * 50)