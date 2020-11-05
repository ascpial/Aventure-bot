import sqlite3
from gestionnaire import monde

class Client(object):
    def __init__(self, user_id, salle, bot):
        self.user_id = user_id
        self.user = user_id
        if self.user == None: pass #destroy the member
        self.salle = monde[salle]
        self.bot = bot
        self.database = Database("base.db", self.bot)
    async def load(self):
        self.user = self.bot.get_user(self.user)
    async def send(self, *args, **kwargs):
        await self.user.send(*args, **kwargs)
    def set_salle(self, salle):
        curseur = self.database.curseur().execute("""UPDATE "clients" SET "salle"="%s" WHERE "id"=%i"""%(salle.id, self.user_id))
        self.database.connection().commit()
        self.salle = salle
        print(salle)

class Database(object):
    def __init__(self, base, bot):
        self.base = base
        self.conn = None
        self.bot  = bot
    def connection(self):
        if self.conn == None: self.conn = sqlite3.Connection(self.base)
        return self.conn
    def curseur(self):
        return self.connection().cursor()
    async def get_client(self, id):
        curseur = self.curseur().execute("select * from clients where id=%i"%id)
        client = curseur.fetchall()
        if len(client) == 0: pass
        else:
            client = Client(client[0][0], client[0][1], self.bot)
            await client.load()
            return client