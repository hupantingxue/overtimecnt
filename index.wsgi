import os

import sae
import sae.const
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert

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

@compiles(Insert)
def append_string(insert, compiler, **kw):
    s = compiler.visit_insert(insert, **kw)
    if 'append_string' in insert.kwargs:
        return s + " " + insert.kwargs['append_string']
    return s

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
        #dbovertime.update().where(dbovertime.c.day==day).values(overtime=1).execute()
        dbovertime.insert(append_string = 'ON DUPLICATE KEY UPDATE overtime=1').execute(month=mon, day=day, overtime=1)
        raise web.seeother('/')

class normal:
    def POST(self):
        mon, day = getTime()
        #n = db.update('overtime', where='day=$day', overtime=0, vars = locals())
        #dbovertime.update().where(dbovertime.c.day==day).values(overtime=0).execute()
        dbovertime.insert(append_string = 'ON DUPLICATE KEY UPDATE overtime=0').execute(month=mon, day=day, overtime=0)
        raise web.seeother('/')

web.config.debug = True
app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)
