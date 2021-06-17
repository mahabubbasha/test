import MySQLdb, pprint

class MultupleDB:
    def __init__(self,username, password, database, host, table, fldname):
        self.user     = username
        self.password = password
        self.db       = database
        self.host     = host
        self.table    = table
        self.fldname  = fldname
        self.conn     = ""

    def Connect_first_db(self):
        self.conn = MySQLdb.connect (host = self.host,
                                     user = self.user,
                                     passwd = self.password,
                                     db = self.db)


    def query(self):
        pp = pprint.PrettyPrinter(indent=4)
        cursor = self.conn.cursor()
        cursor.execute ("select * from %s" % self.table)
        a = cursor.fetchall()
        pp.pprint(a)



t = MultupleDB('howdy', 'pardner', 'howdy', 'univac.juniper.net', 'todo', None)
t.Connect_first_db()
t.query()

print "data from another database\n\n"
y = MultupleDB('howdy', 'pardner', 'howdy', 'univac-dev.juniper.net', 'todo', None)
y.Connect_first_db()
y.query()
