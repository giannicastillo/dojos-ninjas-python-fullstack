from flask_app import app
from flask import render_template,redirect,session, request

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# ======================================
# Index/ home page 
# ======================================

@app.route('/')
def index():
    dojos= Dojo.all_dojos()

    print(dojos)
    for dojo in dojos:
        print(dojo.name)
    return render_template('dojos.html', dojos=dojos)

# =====================================
#POST/CREATE NEW DOJO ON THE MAIN PAGE AND HAVE IT ADD ON TO THE LIST. 
# =====================================
@app.route('/new_dojo', methods=['POST'])
def create_dojo():

    data={
        "name" : request.form["dojo_name"]
    }
    Dojo.add_dojo(data)

    return redirect ('/')



# =====================================
# # and ninja info when a dojo is clicked
# # Matching ninja info w/ SQL with dojoshow.html
# THIS METHOD IS A 2 IN 1 . 1) LINK TO PAGE 2) DISPLAY NINJA INFO
# # =======================================
@app.route('/dojos/<int:id>')
def ninja_info(id):
    data={
        "id" : id
    }
    
    dojos_with_ninjas = Dojo.dojo_with_ninjas(data)
    print(dojos_with_ninjas.ninjas)
    return render_template ("dojoshow.html", dojos = dojos_with_ninjas)

# ==============================================
# Route from main page to  New ninja page using add ninja action on NN HTML
# ============================================

@app.route('/ninjas')
def dojos_btn():
    dojos= Dojo.newninja_dojos()

    print(dojos)
    for dojo in dojos:
        print(dojo.name)
    return render_template('newninja.html', dojos=dojos)
# ===================================
# POST INFO FROM NEW NIJA PAGE && REDIRECT TO DOJOSHOW AFTER CREATING
# ========================================

@app.route('/process_ninja' , methods=['POST'])
def new_ninja():
    data={
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id'],
    }
    Ninja.create_ninja(data)
    return redirect(f"/dojos/{request.form['dojo_id']}")
