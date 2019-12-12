import random

def main():
    times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
    advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
    promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
    "неожиданного праздника", "приятных перемен"]
    generated_prophecies = Generated_Prophecies(Random, times, advices, promises)


def Random(list0):
    for i in list0:
        index = random.randrange(0, len(list0))
        return index

def Generated_Prophecies(Function, list1, list2, list3):
    generated_prophecies = []
    for i in range(15):
        generated_prophecies.append(list1[Function(list1)].title() + ' ' + list2[Function(list2)] + ' ' +  list3[Function(list3)] + '.')
    return generated_prophecies

if __name__ == "__main__":
    main()
