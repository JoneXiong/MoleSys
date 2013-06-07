from peewee import *

database = MySQLDatabase('zkeco_db', **{'passwd': 'root', 'user': 'root'})

class UnknownFieldType(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Checkinout(BaseModel):
    reserved = CharField(null=True, db_column='Reserved')
    sn = IntegerField(null=True, db_column='SN')
    workcode = CharField(null=True, db_column='WorkCode')
    checktime = DateTimeField()
    checktype = CharField(null=True)
    sensorid = CharField(null=True)
    sn_name = CharField(null=True)
    userid = IntegerField()
    verifycode = IntegerField()

    class Meta:
        db_table = 'checkinout'
        
    def __unicode__(self):
        return '%s: %s' % (self.userid, self.checktime)

