from mongoengine import *

connect()


class UserLocation(Document):
    id = IntField(primary_key=True)
    name = StringField()
    location = PointField()
    createdDate = DateTimeField()

    meta = {
        'strict': False,
        'collection': 'location_data',
        'indexes': ['location']
    }

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location['coordinates'],
            'createdDate': self.createdDate
        }
