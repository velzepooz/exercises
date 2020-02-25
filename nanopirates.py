"""
В последнее время вы заметили, что в одном из углов у вас дома плохо ловит wi-fi
сигнал, но провайдер не хочет бесплатно менять вам роутер, ссылаясь на то, что
это просто плохая погода и вообще, мол, Луна в Водолее (что бы это ни
означало). Единственное, о чем вам удалось договориться, — провайдер пойдет
на продолжение разговора, если вы докажете с помощью сертифицированного
измерителя, что показания сигнала после суток наблюдения не выходят на ноль
по сумме или даже их сумма превышает 50 нанопиратов (почему-то ваш
провайдер настаивает именно на такой метрике, я о ней тоже (почти) никогда не
слышал).
Ваш хороший знакомый принес вам модифицированный (но все еще
сертифицированный) детектор сигнала, который записывает показания с
достаточной для этого частотой. Он торопился, и у него не было возможности
нормально подготовить еще и процедуру подсчета данных. Но зато наблюдения,
которые записаны в файле, уже сразу в нанопиратах.
"""


with open('m5-calibration.dat', 'r') as file:
    level = 0
    for line in file:
        level += int(line)
    print(f'level = {level}')
