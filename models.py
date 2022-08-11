from peewee import *

db = PostgresqlDatabase(
    'mistery_shack',
    host = 'localhost',
    port = '5432',
    user = 'dipper',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Monsters(BaseModel):
    name = CharField(max_length=255, null=False)
    description = CharField(max_length=255, null=False)
    weakness = CharField(max_length=255, null=False)


db.create_tables([Monsters])
db.close()