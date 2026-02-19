from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileAllowed

class TodoForm(FlaskForm):

    task = StringField(
        "Task",
        validators=[DataRequired(), Length(max=200)],
        render_kw={"class": "form-control", "placeholder": "Enter your task"}
    )

    image = FileField(
        "Upload Image (Optional)",
        validators=[
            Optional(),
            FileAllowed(["jpg", "jpeg", "png", "gif"], "Images only!")
        ],
        render_kw={"class": "form-control"}
    )

    submit = SubmitField(
        "Add Task",
        render_kw={"class": "btn btn-primary"}
    )
    