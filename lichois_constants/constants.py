import re

from .date_constants import LICHOIS_DATE_FORMAT, LICHOIS_DATETIME_FORMAT
from .date_constants import LICHOIS_SHORT_DATE_FORMAT, LICHOIS_SHORT_DATETIME_FORMAT


MALE = "male"
FEMALE = "female"
OTHER = "other"

YES = "Yes"
NO = "No"
NOT_APPLICABLE = "N/A"

# Status Constants
OPEN = "open"
CLOSED = "closed"
DRAFT = "draft"
PENDING = "pending"
APPROVED = "approved"
ACCEPTED = "accepted"
REJECTED = "rejected"
CANCELLED = "cancelled"
SCHEDULED = "scheduled"
ON_GOING = "on_going"
COMPLETED = "completed"
DEFERRED = "deferred"
STARTED = "started"
ENDED = "ended"
PRESENT = "present"
ABSENT = "absent"

# Document Status
ISSUED = "issued"
NOT_ISSUED = "not_issued"
LOST = "lost"
STOLEN = "stolen"
DAMAGED = "damaged"

# Communication Methods
EMAIL = "email"
SMS = "sms"
POSTAL = "postal"
TELEPHONE = "telephone"
CELLPHONE = "cellphone"

# Identity Types
OMANG = "OMANG"
PASSPORT = "PASSPORT"

# Marital Status
SINGLE = "single"
MARRIED = "married"
WIDOWED = "widowed"
SEPARATED = "separated"
DIVORCED = "divorced"

# Permit Types
WORK = "work"
RESIDENCE = "residence"

# Person Types
APPLICANT = "applicant"
MOTHER = "mother"
FATHER = "father"
CHILD = "child"
GUARDIAN = "guardian"
SPONSOR = "sponsor"
WITNESS = "witness"
DECLARANT = "declarant"
ADOPTIVE_PARENT = "adoptive_parent"
SUBSCRIBER = "subscriber"


UUID_PATTERN = re.compile(
    '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}|'
    '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
VIEW = 'VIEW'
WEEKDAYS = 'weekdays'
WEEKENDS = 'weekends'
YES = 'Yes'
