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
        mon, day = getTime()
        overs = db.select('overtime', where='month=$mon', order='day', vars=locals())
        return render.index(overs)

class over:
    def POST(self):
        mon, day = getTime()
        n = db.update('overtime', where='day=$day', overtime=1, vars = locals())
        raise web.seeother('/')

class normal:
    def POST(self):
        mon, day = getTime()
        n = db.update('overtime', where='day=$day', overtime=0, vars = locals())
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()        
