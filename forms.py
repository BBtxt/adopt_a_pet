from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[InputRequired(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Optional()])
    available = BooleanField("Available for adoption?", default=True, validators=[InputRequired()])

    
class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional()],
    )

    available = BooleanField("Available?")