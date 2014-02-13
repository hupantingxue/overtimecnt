import os
import web
import MySQLdb
import time

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

urls = ('/', 'index',
        '/over', 'over',
        '/normal', 'normal')

db = web.database(dbn='mysql', user='db_user', pw='db_pwd', db='db_dbname')

def getTime():
    t=time.localtime(time.time())
    mon = time.strftime("%Y%m", t)
    day = time.strftime("%Y%m%d", t)
    return mon, day

class index:
    def GET(self):
        _mon, _day = getTime()
        try:
            i = web.input()
            mon = i.month
        except Exception as e:
            mon = _mon
        overs = db.select('overtime', where='month=$mon', order='day', vars=locals())
        return render.index(overs)

class over:
    def POST(self):
        mon, myday = getTime()
        i = web.input()
        overday = i.overday
        if "0" == overday:
            overday = myday
        n = db.update('overtime', where='day=$overday', overtime=1, vars = locals())
        #n = db.insert('overtime', overtime=1, day=overday, month=mon)
        raise web.seeother('/')

class normal:
    def POST(self):
        mon, myday = getTime()
        i = web.input()
        overday = i.overday
        if "0" == overday:
            overday = myday
        mon, day = getTime()
        n = db.update('overtime', where='day=$overday', overtime=0, vars = locals())
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
