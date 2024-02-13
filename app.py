from flask import Flask, redirect, render_template, request
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhhh. its a secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

@app.route('/')
def home_page():
    """Show home page"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    """Show add pet form"""

    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {key: value for key, value in form.data.items() if key != 'csrf_token'}
        new_pet = Pet(**data)
        try:
            db.session.add(new_pet)
            db.session.commit()
        except:
            db.session.rollback()
            logging.error('Error adding pet')
            logging.error(str(e))
        
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)    
    
@app.route('/pet/<int:pet_id>', methods=['GET', 'POST'])
def show_pet(pet_id):
    """Show pet details"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)

@app.route("/edit/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        
        return redirect(f"/pet/{pet_id}")

    else:
        # failed; re-present form for editing
        return render_template("edit_form.html", form=form, pet=pet)

@app.route('/delete/<id>', methods=['POST'])
def delete_route(id):
    if request.form.get('_method') == 'DELETE':
        pet = Pet.query.get(id)
        if pet:
            db.session.delete(pet)
            db.session.commit()
            return redirect('/')
    else:
        return render_template('404.html')
    
    
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()