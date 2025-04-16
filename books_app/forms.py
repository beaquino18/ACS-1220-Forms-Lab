from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')


class AuthorForm(FlaskForm):
    """Form to create an author."""
    name = StringField('Author',
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Author's name needs to be between 3 and 80 chars")
        ])
    
    biography = TextAreaField('Biography', 
        validators=[ Length(min=3, max=200, message="Biography needs to be between 3 and 200 chars")])
    
    date_of_birth = DateField("Date of Birth", validators=[DataRequired()])
    books = QuerySelectMultipleField('Books', query_factory=lambda: Book.query)
    submit = SubmitField('Submit')

    # Fill out the fields in this class for:
    # - the author's name
    # - the author's biography (hint: use a TextAreaField)
    # - a submit button

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.


class GenreForm(FlaskForm):
    """Form to create a genre."""
    name = StringField('Genre',
        validators=[
            DataRequired(),
            Length(min=3, max=200, message="Genre name needs to be between 3 and 80 chars")
        ])
    books = QuerySelectMultipleField('Books', query_factory=lambda: Book.query)
    submit = SubmitField('Submit')

    # Fill out the fields in this class for:
    # - the genre's name (e.g. fiction, non-fiction, etc)
    # - a submit button

class UserForm(FlaskForm):
    """Form to create a user."""
    username = StringField('Username',
        validators=[
            DataRequired(),
            Length(min=3, max=200, message="Username must be between 3 and 80 chars")
        ])
    
    favorite_books = QuerySelectMultipleField('Favorite Books', query_factory=lambda: Book.query)
    submit = SubmitField('Submit')
