from django.conf import settings

# for strftime formatting in LICHOIS messages etc.

timezone = ' %Z' if settings.USE_TZ else ''
try:
    LICHOIS_DATE_FORMAT = settings.LICHOIS_DATE_FORMAT
except AttributeError:
    LICHOIS_DATE_FORMAT = '%A %d %b %Y'

try:
    LICHOIS_DATETIME_FORMAT = settings.LICHOIS_DATETIME_FORMAT
except AttributeError:
    LICHOIS_DATETIME_FORMAT = f'%A %d %b %Y %I:%M%p{timezone}'

try:
    LICHOIS_SHORT_DATE_FORMAT = settings.LICHOIS_SHORT_DATE_FORMAT
except AttributeError:
    LICHOIS_SHORT_DATE_FORMAT = '%Y-%m-%d'

try:
    LICHOIS_SHORT_DATETIME_FORMAT = settings.LICHOIS_SHORT_DATETIME_FORMAT
except AttributeError:
    LICHOIS_SHORT_DATETIME_FORMAT = f'%Y-%m-%d %H:%M{timezone}'
