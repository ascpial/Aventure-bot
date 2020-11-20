import sqlite3
from salles_gestionnaire import *

monde = Salles()
creer_salles("salles", monde)
monde.create()

class Client(object):
    def __init__(self, user_id, salle, nom, activity, bot):
        self.user_id = user_id
        self.user = user_id
        if self.user == None: pass #Supprime le membre
        self.salle = monde[salle]
        self.nom = nom
        self.activity = activity
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
    def set_statut(self, statut):
        curseur = self.database.curseur().execute("""UPDATE "clients" SET "activity"="%s" WHERE "id"=%i"""%(statut, self.user_id))
        self.database.connection().commit()
        self.statut = statut

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
    async def get_client(self, client_user):
        curseur = self.curseur().execute("select * from clients where id=%i"%client_user.id)
        client = curseur.fetchall()
        if len(client) == 0: return None
        client = Client(client[0][0], client[0][1], client[0][2], client[0][3], self.bot)
        await client.load()
        return client
    def create_user(self, user):
        self.curseur().execute("""insert into clients values (%i, "%s", "%s", "")"""%(user.id, 'salles/maison/balcon.json', user.name))
        self.connection().commit()
        curseur = self.curseur().execute("select * from clients where id=%i"%user.id)
        client = curseur.fetchall()