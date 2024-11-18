import random

# Словарь с более сложными русскими словами и их переводами на английский
words = {
    "достижение": "accomplishment",
    "захватывающий": "breathtaking",
    "сознание": "consciousness",
    "решимость": "determination",
    "восторженный": "enthusiastic",
    "очаровательный": "fascinating",
    "невероятный": "incredible",
    "тщательный": "meticulous",
    "восприятие": "perception",
    "устойчивость": "resilience",
    "существенный": "substantial",
    "преобразование": "transformation",
    "беспрецедентный": "unprecedented",
    "уязвимый": "vulnerable",
    "мудрость": "wisdom"
}

start = input("Введите 'start' для начала: ").strip().lower()

if start != "start":
    print("Вы не ввели команду 'start'. Завершение программы.")
else:
    # Функция для изучения слов
    def learn_words(words):
        # Создаем список неповторяющихся слов и перемешиваем
        words_list = list(words.items())
        random.shuffle(words_list)
        
        total_points = 0  # Общий счет
        max_points = 100  # Максимум баллов
        num_words = len(words_list)  # Количество слов
        points_per_word = max_points / num_words  # Баллы за одно слово
        
        # Начало изучения
        learned_words = set()
        
        while len(learned_words) < num_words:
            # Выбираем следующее слово
            russian_word, english_word = words_list[len(learned_words)]
            print(f"Переведите слово на английский: '{russian_word}'")
            
            # Пользователь вводит перевод
            answer = input("Ваш ответ: ").strip().lower()
            
            # Проверка правильности ответа и начисление баллов
            if answer == english_word.lower():
                total_points += points_per_word
            
            # Добавляем слово в список изученных
            learned_words.add((russian_word, english_word))
        
        # Итоговый результат
        print(f"\nВы закончили изучение слов.")
        print(f"Ваш итоговый счет: {int(total_points)} из 100 баллов.")

    # Запуск функции
    learn_words(words)
