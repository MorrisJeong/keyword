import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import operator
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
font_path = '/usr/share/fonts/'

di =dict()
li=list()
for page in range(0,1000):
    url = 'https://www.clien.net/service/board/park?&od=T31&po='+str(page)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    titles = soup.find_all('div',{'class':'list_item'})
    for title in titles:
        cons=title.find_all('span')
        for con in cons:
            if con.find("span","timestamp") is not None:
                time=con.find("span","timestamp").text.split(' ')[0]
                #print(time)
                day=time.split('-')[2]
                #print(day)
                if(str(day) =='08'):
                    #sorteddict = sorted(di.items(), key=operator.itemgetter(1), reverse = True)
                    #print(sorteddict)
                    wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', background_color='white', width=800, height=600).generate(' '.join(li))
                    #worldcloud = wc.generate(di)
                    stopwords = set(STOPWORDS)
                    stopwords.add("jpg")
                    stopwords.add("gif")
                    plt.imshow(wc, interpolation='bilinear')
                    plt.axis("off")
                    plt.show()
                    #quit()
            if con.get('title') is not None:
                contexts=con.get('title').split(' ')
                for context in contexts:
                    di[context]=di.get(context,0)+1
                    li.append(context)
                    print(context)
                    print(di[context])

#날짜에 해당하는 데이터 수집
#날짜 오늘날짜 자동으로 받아오게 해야함
#제목 데이터 클라우드 만들기 해야함
