from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField,\
     DateTimeField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, AnyOf, URL, Regexp,\
     ValidationError
from enum import Enum
import re

# To add a show
class ShowForm(Form):
    artist_id = StringField(
        'artist_id', validators=[DataRequired()]
    )
    venue_id = StringField(
        'venue_id', validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time', validators=[DataRequired()], default= datetime.today()
    )
    submit = SubmitField('Add Show')

# Enumerate cities in US
class UnitedState(Enum):
    AL = 'Alabama'
    AK = 'Alaska'
    AZ = 'Arizona'
    AR = 'Arkansas'
    CA = 'California'
    CO = 'Colorado'
    CT = 'Connecticut'
    DE = 'Delaware'
    FL = 'Florida'
    GA = 'Georgia'
    HI = 'Hawaii'
    ID = 'Idaho'
    IL = 'Illinois'
    IN = 'Indiana'
    IA = 'Iowa'
    KS = 'Kansas'
    KY = 'Kentucky'
    LA = 'Louisiana'
    ME = 'Maine'
    MD = 'Maryland'
    MA = 'Massachusetts'
    MI = 'Michigan'
    MN = 'Minnesota'
    MS = 'Mississippi'
    MO = 'Missouri'
    MT = 'Montana'
    NE = 'Nebraska'
    NV = 'Nevada'
    NH = 'New Hampshire'
    NJ = 'New Jersey'
    NM = 'New Mexico'
    NY = 'New York'
    NC = 'North Carolina'
    ND = 'North Dakota'
    OH = 'Ohio'
    OK = 'Oklahoma'
    OR = 'Oregon'
    PA = 'Pennsylvania'
    RI = 'Rhode Island'
    SC = 'South Carolina'
    SD = 'South Dakota'
    TN = 'Tennessee'
    TX = 'Texas'
    UT = 'Utah'
    VT = 'Vermont'
    VA = 'Virginia'
    WA = 'Washington'
    WV = 'West Virginia'
    WI = 'Wisconsin'
    WY = 'Wyoming'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.name) for choice in cls]

# Enumerate Genre
class Genre(Enum):
    Alternative = 'Alternative'
    Blues = 'Blues'
    Classical = 'Classical'
    Country = 'Country'
    Electronic = 'Electronic'
    Folk = 'Folk'
    Funk = 'Funk'
    Hip_Hop = 'Hip-Hop'
    Heavy_Metal = 'Heavy Metal'
    Instrumental = 'Instrumental'
    Jazz = 'Jazz'
    Musical_Theatre = 'Musical Theatre'
    Pop = 'Pop'
    Punk = 'Punk'
    R_and_B = 'R&B'
    Rock_n_Roll = 'Rock n Roll'
    Soul = 'Soul'
    Other = 'Other'

    @classmethod
    def choices(cls):
        return [(choice.value, choice.value) for choice in cls]

# Validate phone number
def validate_phone(form, field):
    if not re.search(r"^[0-9]*$", field.data):
        raise ValidationError("Phone number should only contain digits.")

# Form to add a venue
class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired(),
        AnyOf([(choice.name) for choice in UnitedState])],
        choices=UnitedState.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    image_link = StringField(
        'image_link'
    )
    website_link = StringField(
        'website_link', validators=[URL()]
    )
    seeking_talent = BooleanField( 'seeking_talent' )
    seeking_description = StringField(
        'seeking_description'
    )

# Form to add artist
class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired(),
        AnyOf([(choice.name) for choice in UnitedState])], 
        choices=UnitedState.choices()
    )
    phone = StringField(
        'phone'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    image_link = StringField(
        'image_link'
    )
    website_link = StringField(
        'website_link', validators=[URL()]
    )
    seeking_venue = BooleanField( 
        'seeking_venue'
    )
    seeking_description = StringField(
        'seeking_description'
    )