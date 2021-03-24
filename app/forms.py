
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, TimeField, SubmitField, BooleanField, SelectField, IntegerField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea
from .setup import query

class PropertyForm(FlaskForm):
    title     = StringField(id = 'title', validators=[DataRequired()], render_kw={"placeholder":"Title..."}, label = "Property Title")
    no_bath   = IntegerField(id = 'no_bath', validators=[DataRequired()], render_kw={"placeholder":"Number of bathrooms..."}, label = "No. of Bathrooms")
    no_bed    = IntegerField(id = 'no_bed', validators=[DataRequired()], render_kw={"placeholder":"Number of bedrooms..."}, label = "No. of Rooms")
    location  = StringField(id = 'location', validators=[DataRequired()], render_kw={"placeholder":"Location..."}, label = "Location")
    price     = StringField(id = 'price', validators=[DataRequired()], render_kw={"placeholder":"Price..."}, label = "Price")
    typ       = SelectField(id = "typ", validators=[DataRequired()], choices = ["Select a type...", "Apartment", "House"], label = "Property Type")
    desc      = StringField(id = "desc", widget = TextArea(), validators= [DataRequired()], render_kw = {"placeholder":"A short description of your property...", "rows":4}, label = "Description")
    media     = FileField(id = "image", validators=[], label = "Photo", render_kw = {"data-buttonText":"Your label here."})
    email     = StringField(id = "email", validators=[], render_kw={"placeholder":"Email..."})
    submit    = SubmitField("Add Property")
