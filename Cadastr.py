"""
В приложенном файле находятся координаты неких квадратов на абстрактной
карте. Каждая строчка задает один такой квадрат. Формат записи:
ID#1560 :: 530,569 :: 17x27
Здесь указаны, соответственно, ID участка, его горные координаты и площадь. В
данном примере это участок номер 1560, расположенный в координатах x=530,
y=569 и размерами 17 на 27.
Вам надо распаковать, прочесть и обработать оба. Вопросы внизу подразумевают,
что вы прочитали и обработали оба файла.
Да, кстати! Что-то случилось с форматом передачи, и файл пришел к вам битый.
Примерно каждая седьмая строчка содержит какой-то другой набор почти
случайных символов. Вам надо игнорировать их при обработке.
"""


import zipfile


class Cadastr:

    def __init__(self, archive1, file1, archive2, file2):
        self.patern = ' :: '
        self.archive1 = archive1
        self.file1 = file1
        self.archive2 = archive2
        self.file2 = file2

    def extract_file(self):
        zipfile.ZipFile(self.archive1, 'r').extractall()
        zipfile.ZipFile(self.archive2, 'r').extractall()

    def get_info(self):
        self.extract_file()
        objects = []
        with open(self.file1, 'r') as fl:
            for line in fl:
                line_lst = line.strip().split(self.patern)
                if len(line_lst) == 1:
                    pass
                else:
                    id = line_lst[0]
                    x = line_lst[1].split(',')[0]
                    y = line_lst[1].split(',')[1]
                    size = line_lst[2]
                    objects.append([id, x, y, size])
        with open(self.file2, 'r') as fl:
            for line in fl:
                line_lst = line.strip().split(self.patern)
                if len(line_lst) == 1:
                    pass
                else:
                    id = line_lst[0]
                    x = line_lst[1].split(',')[0]
                    y = line_lst[1].split(',')[1]
                    size = line_lst[2]
                    objects.append([id, x, y, size])
        return objects

    def area_count(self, lst):
        parameters = []
        area = []
        for line in lst:
            parameters.append(line[3].split('x'))
        for i in parameters:
            area.append(int(i[0]) * int(i[1]))
        return area

    def middle_area(self, lst):
        area = self.area_count(lst)
        return int(sum(area) / len(area))

    def max_id(self, lst):
        area = self.area_count(lst)
        max_id = max(area)
        index = area.index(max_id)
        return lst[index][0]

    def longest_area(self, lst):
        parameters = []
        long = []
        for line in lst:
            parameters.append(line[3].split('x'))
        for high, width in parameters:
            if int(high) > int(width):
                long.append(int(high) / int(width))
            elif high < width:
                long.append(int(width) / int(high))
        max_long = int(max(long))
        index = long.index(max_long)
        return lst[index][0]



a = Cadastr('[sharewood.biz] m7-map-1.zip', 'm7-map-1.txt', '[sharewood.biz] m7-map-2.zip', 'm7-map-2.txt')
g = a.get_info()
print(a.longest_area(g))









