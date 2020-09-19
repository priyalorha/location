from datetime import datetime
from pytz import timezone

from models.location import UserLocation, GeoPointField


def insert_user_location(**kwargs):
    UserLocation(name=kwargs['name'],
                 id=kwargs['id'],
                 location=[kwargs['latitude'], kwargs['longitude']],
                 createdDate=datetime.now()
                 ).save()


def fetch_user_location(radius: float,
                        latitude: float,
                        longitude: float) -> [UserLocation] or None:
    IST = timezone('Asia/Kolkata')
    time = datetime.now(tz=IST)

    try:
        return UserLocation.objects(location__geo_within_sphere=[[latitude, longitude], radius])
    except Exception:
        return None


