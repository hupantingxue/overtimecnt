import os

import sae
import sae.const
from sqlalchemy import *
from sqlalchemy.pool import NullPool

import web
import time

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

urls = ('/', 'index',
        '/over', 'over',
        '/normal', 'normal')

dburl = 'mysql://%(user)s:%(pass)s@%(host)s:%(port)s/%(db)s' % \
    {
        'user' : sae.const.MYSQL_USER,
        'pass' : sae.const.MYSQL_PASS,
        'host' : sae.const.MYSQL_HOST,
        'port' : sae.const.MYSQL_PORT,
        'db' : sae.const.MYSQL_DB,
   }
db = create_engine(dburl, connect_args={'charset':'utf8'}, poolclass=NullPool)
metadata = MetaData(db)
dbovertime = Table('overtime', metadata, autoload=True)

#nport = int(sae.const.MYSQL_PORT)
#db = web.database(dbn='mysql', host=sae.const.MYSQL_HOST, port=nport, user=sae.const.MYSQL_USER, pw=sae.const.MYSQL_PASS, db=sae.const.MYSQL_DB)

def getTime():
    t=time.localtime(time.time())
    mon = time.strftime("%Y%m", t)
    day = time.strftime("%Y%m%d", t)
    return mon, day

class index:
    def GET(self):
        mon, day = getTime()
        #overs = db.select('overtime', where='month=$mon', order='day', vars=locals())
        overs = dbovertime.select().where(dbovertime.c.month==mon).order_by(dbovertime.c.day).execute()
        return render.index(overs)

class over:
    def POST(self):
        mon, day = getTime()
        #n = db.update('overtime', where='day=$day', overtime=1, vars = locals())
        dbovertime.update().where(dbovertime.c.day==day).values(overtime=1).execute()
        raise web.seeother('/')

class normal:
    def POST(self):
        mon, day = getTime()
        #n = db.update('overtime', where='day=$day', overtime=0, vars = locals())
        dbovertime.update().where(dbovertime.c.day==day).values(overtime=0).execute()
        raise web.seeother('/')

web.config.debug = True
app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)
