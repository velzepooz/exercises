def make_header(word="Заголовок", tag="h1"):
    return "<%s>%s:</%s>" % (tag, word.capitalize(), tag)


print(make_header("важное сообщение"))
h1 = make_header
print(h1("внимательно"))


def make_header(word="Заголовок", tag="h1"):
    def f():
        return "<%s>%s:</%s>" % (tag, word.capitalize(), tag)

    return f()


print(make_header("важное сообщение"))


def make_tag_f(tag="h1"):
    def f(word):
        return "< %s>%s:</%s>" % (tag, word.capitalize(), tag)

    return f


h3 = make_tag_f(tag="h3")
print(h3("внимательно"))


def h1_result(f):
    def wrapper():
        res = f()
        return "<h1>" + res + ":</h1>"

    return wrapper


@h1_result
def my_function():
    return "Следите за руками"


print(my_function())

import time


class LoudStopwatch:

    def __enter__(self):
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        self.end = time.process_time()
        self.delta = self.end - self.start


from urllib.request import urlopen


url = "http://www.ya.ru"
with LoudStopwatch() as s:
    f = urlopen(url)
    f.read()

print("Запрос выполнился за %.03f секунд" % s.delta)
