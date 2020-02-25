"""
Вам поручили написать скрипт, который анализирует эти результаты.
К скрипту предъявили следующие требования:
1. Посчитать в файле с логами все ip с частотами.
2. Найти максимально часто встречающийся ip адрес.
3. Посчитать процент вклада запросов с этого ip от общего числа запросов.
4. Найти последнюю запись в логах с этим ip, выяснить, какой был useragent у
такой записи.
5. Cформировать dict с этими данными.
"""

import pandas


def antibot():
    data = pandas.read_csv('m5-access-log-all.csv')
    max_ip_count = data['ip'].value_counts()[0]
    max_ip = data['ip'].value_counts().keys()[0]
    all_ip_count = data['ip'].count()
    percentage = round((max_ip_count / all_ip_count) * 100, 2)
    timestamp = data[data['ip'] == max_ip].max()[0]
    user_agent = data[data['ip'] == max_ip].max()[2]
    return {
        'ip': f'{max_ip}',
        'fraction': percentage,
        'count': max_ip_count,
        'last': {
            'agent': f'{user_agent}',
            'timestamp': f'{timestamp}'
        }
    }
