from horoscope import generate_prophecies
from datetime import datetime as dt

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]

def generate_page(head, body):
    page = f"<html> {head} {body} </html>"
    return page

def generate_head(title):
    head = f"""<head>
    <meta charset='utf-8'>
    <title> {title}</title>
    </head>
    """
    return head

def generate_body(header, link, link_descr, img, times_name, advices_name, promises_name, times, advices, promises):
    body = f"<h1>{header}</h1>"
    body = body + f"<img src='{img}'/>"
    anchor = f"<a href='{link}'>{link_descr}</a>"
    body = body + f"<ol><li>{times_name}<ul>"
    for i in times:
        body = body + f"<li>{i}</li>"
    body = body + f"</ul></li>" + f"<li>{advices_name}<ul>"
    for i in advices:
        body = body + f"<li>{i}</li>"
    body = body + f"</ul></li><li>{promises_name}<ul>"
    for i in promises:
        body = body + f"<li>{i}</li>"
    body = body + f"</ul></li></ol>"
    return f"<body>{body}{anchor}</body>"

def save_page(title, header, link, link_descr, img, times_name, advices_name, promises_name, output="about.html"):
    fp = open(output, "w")
    today = dt.now().date()
    page = generate_page(
    head=generate_head(title),
    body=generate_body(header=header, link=link, link_descr=link_descr, img=img, times_name=times_name, advices_name=advices_name, promises_name=promises_name, times=times, advices=advices, promises=promises)
    )
    print(page, file = fp)
    fp.close()

today = dt.now().date()
save_page(
title="Реализация",
header="О чем все это",
times_name="Время дня",
advices_name="Глаголы",
promises_name="Обещания",
img = "/protivostoychie-znaki-zodiaca.jpg",
link="/index.html",
link_descr="На Главную",
)