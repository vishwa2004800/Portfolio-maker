from flask import Flask,render_template, request,session
import os
import uuid
app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/design")
def design():
    return render_template("design.html")

@app.route('/form/<string:design>', methods = ['GET','POST'])
def form(design):
    session["design_sess"]  = design
    return render_template("form.html")

@app.route('/upload', methods = ['GET','POST'])
def upload():
    design_upload = session.get("design_sess")
    if design_upload == "design1":
        design_name = "design1.html"
    elif design_upload == "design2":
        design_name = "design2.html"
    if request.method == "POST":
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        collegename = request.form.get('collegename')
        about = request.form.get('about')
        prj1 = request.form.get('prj1')
        prj2 = request.form.get('prj2')
        prj3 = request.form.get('prj3')
     
        print(firstname)
        print(lastname)
        print(email)
        print(phone)
        print(collegename)
        print(about)
        print(prj1)
        print(prj2 )
        print(prj3)
     
     
        
        key = uuid.uuid1()

        img = request.files["dp"]
        img.save(f"static/images/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")
    return render_template(design_name, dname = firstname, img = img_new_name,dabout = about,dproject1 = prj1,dproject2=prj2,dproject3 = prj3,
                           demail = email,dphone = phone)


app.run(debug=True)