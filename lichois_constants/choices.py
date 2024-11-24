from django.utils.translation import gettext as _

from .constants import (
    MALE,
    FEMALE,
    OTHER,

    # Basic Response Constants
    YES,
    NO,
    NOT_APPLICABLE,

    # Status Constants
    OPEN,
    CLOSED,
    DRAFT,
    PENDING,
    APPROVED,
    ACCEPTED,
    REJECTED,
    CANCELLED,
    SCHEDULED,
    ON_GOING,
    COMPLETED,
    DEFERRED,
    STARTED,
    ENDED,
    PRESENT,
    ABSENT,

    # Document Status
    ISSUED,
    NOT_ISSUED,
    LOST,
    STOLEN,
    DAMAGED,

    # Communication Methods
    EMAIL,
    SMS,
    POSTAL,
    TELEPHONE,
    CELLPHONE,

    # Identity Types
    OMANG,
    PASSPORT,
    DRIVERS_LICENSE,
    OMANG_RECEIPT,
    OTHER_ID,

    # Marital Status
    SINGLE,
    MARRIED,
    WIDOWED,
    SEPARATED,
    DIVORCED,

    # Permit Types
    WORK,
    RESIDENCE,

    # Person Types
    APPLICANT,
    MOTHER,
    FATHER,
    CHILD,
    GUARDIAN,
    SPONSOR,
    WITNESS,
    DECLARANT,
    ADOPTIVE_PARENT,
    SUBSCRIBER,
    OFFICER,
    DEPENDENT,
    VOLUNTEER,
    STUDENT,
    IMMIGRANT,
    MISSIONARY,

    # Education Levels
    JUNIOR_SCHOOL,
    ASSOCIATE_DEGREE,
    BACHELORS_DEGREE,
    MASTERS_DEGREE,
    DOCTORATE,
    DIPLOMA,
    CERTIFICATE,
    VOCATIONAL,
    PROFESSIONAL_DEGREE,
    TECHNICAL_DEGREE,
    POSTGRADUATE_CERTIFICATE,
    OTHER_EDUCATION,

    # Duration Types
    YEARS,
    MONTHS,
    WEEKS,
    DAYS,
    PERMANENT,
    EMERGENCY_SHORT,
    EMERGENCY_MEDIUM,
    EMERGENCY_LONG,

    # Application Types
    INITIAL,
    RENEWAL,
    REPLACEMENT,
    APPEAL,
    CANCELLATION,
    REVIEW,
    RECONSIDERATION,

    # Applicant Types
    EMPLOYEE,
    INVESTOR,

    # Other Constants
    UUID_PATTERN,
    VIEW,
    WEEKDAYS,
    WEEKENDS,
    ANYTIME
)


COUNTRY = (
    ('botswana', 'Botswana'),
    ('zimbabwe', 'Zimbabwe'),
    ('rsa', 'South Africa'),
    ('zambia', 'Zambia'),
    ('namibia', 'Namibia'),
    ('nigeria', 'Nigeria'),
    ('china', 'China'),
    ('india', 'India'),
    ('OTHER', 'Other'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('AnyDay', 'Any day'),
)

GENDER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
)

IDENTITY_TYPE = (
    (OMANG, 'Omang'),
    ('DRIVERS', 'Driver\'s License'),
    ('PASSPORT', 'Passport'),
    ('OMANG_RCPT', 'Omang Receipt'),
    (OTHER, 'Other'),
)


TIME_OF_WEEK = (
    (WEEKDAYS, 'Weekdays'),
    (WEEKENDS, 'Weekends'),
    (ANYTIME, 'Anytime')
)


TIME_UNITS = (
    ('TODAY', 'Today'),
    ('DAYS', 'Days'),
    ('WEEKS', 'Weeks'),
    ('MONTHS', 'Months'),
    ('YEARS', 'Years'),
)

YES_NO = (
    (YES, _(YES)),
    (NO, _(NO)),
)


YES_NO_NA = (
    (YES, YES),
    (NO, NO),
    (NOT_APPLICABLE, 'Not applicable'),
)

# TODO: update choices

COMM_METHODS = (("email", "E-mail"), ("sms", "SMS"), ("postal", "Post"))

DATE_ESTIMATED_NA = (
    (NOT_APPLICABLE, "Not applicable"),
    ("not_estimated", "No."),
    ("D", "Yes, estimated the Day"),
    ("MD", "Yes, estimated Month and Day"),
    ("YMD", "Yes, estimated Year, Month and Day"),
)

DATE_ESTIMATED = (
    ("-", "No"),
    ("D", "Yes, estimated the Day"),
    ("MD", "Yes, estimated Month and Day"),
    ("YMD", "Yes, estimated Year, Month and Day"),
)

GENDER = (("male", "Male"), ("female", "Female"), ("other", "OTHER"))

IDENTITY_TYPE = (
    ("OMANG", "Omang"),
    ("DRIVERS", "Driver's License"),
    ("PASSPORT", "Passport"),
    ("OMANG_RCPT", "Omang Receipt"),
    ("OTHER", "Other"),
)

MARITAL_STATUS = (
    ("single", "Single"),
    ("married", "Married"),
    ("widowed", "Widowed"),
    ("separated", "Separated"),
    ("divorced", "Divorced"),
)

PERMIT_TYPE = (("work", "Work"), ("residence", "Residence"))

POSTAL_PREFIX = (
    ("VB#", "VB#"),
    ("private_bag", "Private Bag"),
    ("p_o_box", "P. O. Box"),
)

PREFERRED_METHOD_COMM = (("sms", "SMS"), ("post", "POST"), ("email", "EMAIL"))
REASONS_PERMIT = (
    ("dependent", "Dependent"),
    ("volunteer", "Volunteer"),
    ("student", "Student"),
    ("immigrant", "Immigrant"),
    ("missionary", "Missionary"),
)

REPORT_STATUS = (
    (OPEN, _("Open. Some information is still pending.")),
    (CLOSED, _("Closed. This report is complete")),
)

YES_NO = ((YES, _("Yes")), (NO, _("No")))

CERTIFICATE_STATUS = (
    (ISSUED, _("Issued")),
    (NOT_ISSUED, _("Not Issued")),
    (LOST, _("Lost")),
    (STOLEN, _("Stolen")),
    (DAMAGED, _("Damaged")),
)

APPEAL_TYPE = (
    (APPEAL, _("Appeal")),
    (REVIEW, _("Review")),
    (RENEWAL, _("Renewal")),
    (RECONSIDERATION, _("Reconsideration")),
)

APPEAL_STATUS = (
    (PENDING, _("Pending")),
    (REJECTED, _("Rejected")),
    (ACCEPTED, _("Accepted")),
)

EMERGENCY_PERIOD = (
    (EMERGENCY_SHORT, _("1 - 14 days")),
    (EMERGENCY_MEDIUM, _("15 - 90 days")),
    (EMERGENCY_LONG, _("6 months")),
)

SUBMITTER_TYPE = ((APPLICANT, _("Applicant")), (OFFICER, _("Officer")))

PERSON_TYPE = (
    (APPLICANT, _("Applicant")),
    (MOTHER, _("Mother")),
    (FATHER, _("Father")),
    (CHILD, _("Child")),
    (GUARDIAN, _("Guardian")),
)

APPLICANT_TYPE = (
    (EMPLOYEE, _("Employee")),
    (INVESTOR, _("Investor"))
)