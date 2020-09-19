import unittest
from pytz import timezone
from datetime import datetime

from main import fetch_user_location, insert_user_location
from models.location import UserLocation
from mongoengine import disconnect, connect


class TestLocation(unittest.TestCase):
    def setUp(self) -> None:
        IST = timezone('Asia/Kolkata')
        self.time = datetime.now(tz=IST)
        UserLocation(id=7,
                     name='Priya',
                     location=[78.233, 7.12],
                     createdDate=self.time).save()

    @classmethod
    def setUpClass(cls):
        disconnect()
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_location_document(self):
        ob = UserLocation.objects(name='Priya'). \
            order_by('-createdDate')[0]
        self.assertTrue(ob.location, [78.233, 7.12])

    # def test_fetch_user_location(self):
    #     IST = timezone('Asia/Kolkata')
    #     time = datetime.now(tz=IST)
    #     var = {'id': 19,
    #            'name': 'Priya',
    #            'latitude': 1.971599,
    #            'longitude': 7.594566,
    #            'createdDate': time}
    #
    #     insert_user_location(**var)
    #
    #     var = {'id': 29,
    #            'name': 'Priya',
    #            'latitude': 2.971599,
    #            'longitude': 3.594566,
    #            'createdDate': time}
    #
    #     insert_user_location(**var)
    #
    #     var = {'id': 39,
    #            'name': 'Priya',
    #            'latitude': 5.971599,
    #            'longitude': 7.594566,
    #            'createdDate': time}
    #
    #     insert_user_location(**var)
    #
    #     var = {'id': 49,
    #            'name': 'Priya',
    #            'latitude': 12.971599,
    #            'longitude': 73.594566,
    #            'createdDate': time}
    #
    #     insert_user_location(**var)
    #
    #     ob = fetch_user_location(12.95, 77, 0)
    #     for i in ob:
    #         print(i.to_dict())


if __name__ == '__main__':
    unittest.main()
