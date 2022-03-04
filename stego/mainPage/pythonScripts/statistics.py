from counter_bytes_tags2 import contadortags
from counter_bytes_tags2 import contadorcomillas
from attPosition import total_capacity
import requests
from requests.exceptions import ConnectionError
import html
import pandas as pd
import matplotlib.pyplot as plt
import attPosition import count_total as count_total_att

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

'''webpage_list=['https://www.google.com/','https://www.youtube.com/','https://www.facebook.com/','https://twitter.com/','https://www.instagram.com/','http://www.baidu.com/','https://www.wikipedia.org/','https://yandex.ru/','https://es.yahoo.com/','https://www.elmundo.es/','https://www.whatsapp.com/','https://www.netflix.com/es/','https://www.uc3m.es/Inicio','https://vine.co/','https://www.yahoo.co.jp/','https://outlook.live.com/owa/','https://as.com/','https://zoom.us/','https://www.reddit.com/','https://elpais.com/','https://www.office.com/','https://www.spotify.com/es/','https://vk.com/','https://www.hola.com/','https://www.twitch.tv/','https://www.elperiodico.com/es/','https://www.naver.com/','https://www.bing.com/','https://www.roblox.com/','https://duckduckgo.com/','https://www.elespanol.com/','https://mail.ru/','https://www.pinterest.es/','https://www.defensa.gob.es/','https://www.qq.com/','https://news.yahoo.co.jp/','https://www.fandom.com/','https://www.msn.com/es-es/','https://www.google.com.br/','https://www.globo.com/','https://www.ebay.com/','https://www.rtve.es/','https://www.movistar.es/','https://weather.com/es-ES/tiempo/hoy/l/SPXX0050:1:SP?Goto=Redirected','https://ok.ru/','https://ok.ru/','https://www.bbc.com/','https://www.marca.com/','https://www.sport.es/es/','https://www.casadellibro.com/','https://www.w3schools.com/']'''


def web_counter_tags(webpage_l):
	webpage_number_tags=[]
	for elem in webpage_l:
		'''print(elem)'''
		html = urlopen(elem)
		ey=html.readlines()
		tags=0
		for line in ey:
			tags+=contadortags(line)

		'''print(tags)'''
		webpage_number_tags.append(tags)
	return webpage_number_tags

def web_counter_quotes(webpage_l):
	webpage_number_quotes=[]
	for elem in webpage_l:
		'''print(elem)'''
		html = urlopen(elem)
		ey=html.readlines()
		tags=0
		for line in ey:
			tags+=contadorcomillas(line)

		'''print(tags)'''
		webpage_number_quotes.append(tags)
	return webpage_number_quotes

def web_counter_characters(webpage_l):
	webpage_length=[]
	for elem in webpage_l:
		'''print(elem)'''
		html = urlopen(elem)
		ey=html.readlines()
		tags=0
		size=0
		for line in ey:
			characters=list(line)
			size+=len(characters)

		'''print(size)'''
		webpage_length.append(size)
	return webpage_length

def web_counter_lines(webpage_l):
	webpage_lines=[]
	for elem in webpage_l:
		'''print(elem)'''
		html = urlopen(elem)
		ey=html.readlines()
		tags=0
		lines=0
		for line in ey:
			lines+=1

		'''print(lines)'''
		webpage_lines.append(lines)
	return webpage_lines


def main():

    webpage_list=['https://www.google.com/','https://www.youtube.com/','https://www.facebook.com/','https://twitter.com/']#,'https://www.instagram.com/','http://www.baidu.com/','https://www.wikipedia.org/','https://yandex.ru/','https://es.yahoo.com/','https://www.elmundo.es/','https://www.whatsapp.com/','https://www.netflix.com/es/','https://www.uc3m.es/Inicio','https://vine.co/','https://www.yahoo.co.jp/','https://outlook.live.com/owa/','https://as.com/','https://zoom.us/','https://www.reddit.com/','https://elpais.com/','https://www.office.com/','https://www.spotify.com/es/','https://vk.com/','https://www.hola.com/','https://www.twitch.tv/','https://www.elperiodico.com/es/','https://www.naver.com/','https://www.bing.com/','https://www.roblox.com/','https://duckduckgo.com/','https://www.elespanol.com/','https://mail.ru/','https://www.pinterest.es/','https://www.defensa.gob.es/','https://www.qq.com/','https://news.yahoo.co.jp/','https://www.fandom.com/','https://www.msn.com/es-es/','https://www.google.com.br/','https://www.globo.com/','https://www.ebay.com/','https://www.rtve.es/','https://www.movistar.es/','https://weather.com/es-ES/tiempo/hoy/l/SPXX0050:1:SP?Goto=Redirected','https://ok.ru/','https://ok.ru/','https://www.bbc.com/','https://www.marca.com/','https://www.sport.es/es/','https://www.casadellibro.com/','https://www.w3schools.com/']


    print("COUNTING...")
    lines = web_counter_lines(webpage_list)
    print("lines counted")
    characters = web_counter_characters(webpage_list)
    print("characters counted")
    quotes_cap = web_counter_quotes(webpage_list)
    print("quotes counted")
    tag_cap = web_counter_tags(webpage_list)
    print("tags counted")

    print(characters)
    print(lines)
    print(quotes_cap)
    print(tag_cap)

    df = pd.DataFrame({"page": webpage_list,"characters": characters,"lines": lines, "quotes_cap": quotes_cap, "tag_cap": tag_cap})
    df.to_csv("50topStatistics.csv", index=False)

    df = pd.read_csv("50topStatistics.csv")
    print(df.head())

    df['totalbits'] = df['characters']*8
    # df['att_percentage'] = 100*(df['att_cap']/df['totalbits'])
    df['quotes_percentage'] = 100*(df['quotes_cap']/df['totalbits'])
    df['tag_percentage'] = 100*(df['tag_cap']/df['totalbits'])

    # sort df by totalbits ascending
    df.sort_values('totalbits', ascending=True, inplace=True)


    fig, ax = plt.subplots(figsize=(15,6))
    # plt.plot(df.index.to_list(), df.att_cap.to_list(), label="att encoding")
    ax.plot(df.index.to_list(), df.quotes_percentage.to_list(), label="quote encoding")
    ax.plot(df.index.to_list(), df.tag_percentage.to_list(), label="tag encoding")
    plt.xlabel("Webpage index")
    plt.ylabel("encoding capacity over total capacity (%)")
    plt.title("Average capacity of encoding in top 50 visited pages")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
