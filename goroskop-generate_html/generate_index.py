from horoscope import generate_prophecies
from datetime import datetime as dt

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

def generate_body(header, paragraphs, link, link_descr):
    body = f"<h1>{header}</h1>"
    for p in paragraphs:
        body = body + f"<p>{p}</p>"
    anchor= f"<a href='{link}'>{link_descr}</a>"
    return f"<body>{body}{anchor}</body>"

def save_page(title, header, paragraphs, link, link_descr, output="index.html"):
    fp = open(output, "w")
    today = dt.now().date()
    page = generate_page(
    head=generate_head(title),
    body=generate_body(header=header, paragraphs=paragraphs, link=link, link_descr=link_descr)
    )
    print(page, file = fp)
    fp.close()

today = dt.now().date()
save_page(
title="Гороскоп на сегодня",
header="Что день " + str(today) + " готовит",
paragraphs=generate_prophecies(),
link="/about.html",
link_descr="О реализации",
)