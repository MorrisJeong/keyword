import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import operator
from wordcloud import WordCloud#워드클라우드
import matplotlib.pyplot as plt
from datetime import datetime#오늘날짜
import sys#프로그램 종료

#di =dict()
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
                day=time.split('-')[2]
                #게시판의 날짜 형태가 dd이고 datetime패키지에서 불러낸 날짜는 d형태라서 형태를 맞춰주기 위해 아래 2줄을 추가하였습니다.
                if((datetime.today().day-1)<10):
                    board_day = '0'+str(datetime.today().day-1)
                #해당날짜까지 제목을 dict에 저장한 다음 이를 워드클라우드형태로 나타냄
                if(str(day) == board_day):
                    #(' '.join(li) 는 li에 있는 데이터를 사이에 ' '을 넣어서 모두 이어서 string 형태로 만들어준다 )
                    wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', background_color='white', width=800, height=600).generate(' '.join(li))
                    plt.imshow(wc, interpolation='bilinear')
                    plt.axis("off")
                    plt.show()
                    sys.exit(1)
            if con.get('title') is not None:
                #제목을 스페이스 기준으로 나누고 이를 list에 저장
                contexts=con.get('title').split(' ')
                for context in contexts:
                    #di[context]=di.get(context,0)+1
                    li.append(context)
                    #print(context)
                    #print(di[context])
