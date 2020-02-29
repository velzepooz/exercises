"""
Адепты здорового питания любят считать калории и БЖУ (белки, жиры,
углеводы). Предположим, что мы разрабатываем подобный сервис, и нам нужно
создать классы, которые делают базовую арифметику сложения между
элементами (чтобы можно было определить яблоко с БЖУ = (0, 25, 0) и прибавить
к нему яйцо с БЖУ (13, 11, 1) и, сложив их, получить информацию про свой
завтрак.
Принято считать, что 1 г углеводов и 1 г белка — это 4.2 ккал, а 1 г жира — это 9
ккал. Будем грубо округлять подобные энергетические расчеты до целых.
Определите класс NutritionInfo в окошке внизу со всеми необходимыми методами.
1. Не используйте принты, их никто не читает.
2. Вам нужен один из специальных методов.
3. Чтобы у результата суммы двух NutritionInfo был метод energy, результат
сложения должен быть тоже NutritionInfo.
4. Самый простой способ сделать пункт выше – это в сложении создавать
новый объект с суммой новых значений от обоих слагаемых.
"""


class NutritionInfo:

    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)

    def __add__(self, other):
        return NutritionInfo((self.proteins + other.proteins),
                             (self.carbs + other.carbs), (self.fats + other.fats))


curd = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)
breakfast = apple + curd
print(breakfast.energy())
