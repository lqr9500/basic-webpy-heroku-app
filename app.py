#-*-coding:utf-8 -*-
import urllib2,time,json,web,sys
reload(sys)
sys.setdefaultencoding('utf8')


starttime = time.time()
print
#print 'starttime:\t',starttime

urlhit = 'https://api.douban.com/v2/movie/in_theaters'
content = urllib2.urlopen(urlhit).read()
#print content
callback = json.loads(content)

subjects = callback['subjects']
#print type(subjects)    ###list




def analyze():
    global movies
    movies = []

    for i in subjects:
        #global title,average,name

        rating = i['rating']
        #print type(rating)     #####dict
        average = rating['average']
        title = i['title']
        casts = i['casts']

        #print
        #print
        #print title, '  ', average, 'score'


        castlist = []
        for cast in casts:
            name = cast['name']
            castlist.append(name)
            #print name,

        castname = '&emsp;'.join(castlist)
        #title = u'%s'%title
        #castname = u'%s'%castname
        #title = json.dumps(title, encoding='UTF-8', ensure_ascii=False)
        #castname = json.dumps(castname, encoding='UTF-8', ensure_ascii=False)
        titleandscoredic = {'title': '<br> %s &emsp; %s score <br>%s<br>' % (title, average,castname)}
        #castsdic = {'castsname':'%s' %castlist}
        #moviesdic = titleandscoredic,castsdic

        movies.append(titleandscoredic)
        #movies.append(castsdic)
        #print type(moviesdic)
    print movies

        #test = casts[1]
        #print test
        #print type(test)





analyze()

endtime = time.time()
usetime = endtime-starttime
print '\n','\n''usetime',usetime,'s'




urls = (
    '/(.*)', 'hello'
 )
app = web.application(urls, globals())

class hello:
    def GET(self,name):
        if not name:
            page = '<br><h1>超级聪明大帅逼卢给大傻逼苏的七夕节礼物之电影推荐</h1><br><br>'
            for m in movies:
                page += '%s'%m['title']
        web.header('Content-Type','text/html;charset = utf-8')
        localtimes = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        page = page + '<br><br>更新时间 &emsp; %s'%localtimes
        return page





if __name__ == "__main__":
    #web.httpserver.runsimple(app.wsgifunc(), ('127.0.0.1', 8080))
    app.run()
