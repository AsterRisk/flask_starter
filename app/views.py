"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from .__init__ import app
from .forms import PropertyForm
from .models import Property
import os
from .setup import query

print("--VIEWS.PY--")

###
# Routing for your application.
###

def is_picture(filename: str):
    return filename.endswith('jpg') or filename.endswith('jpeg') or filename.endswith('png') or filename.endswith('webp')

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property/', methods = ["GET", "POST"])
def add_property():
    form = PropertyForm()
    if request.method == "GET":
        return render_template('property.html', form = form)
    else:
        if request.method == "POST":
            
            savepath = None
            if form.validate_on_submit():
                if (form.typ.data == "Select a type..."):
                    flash("Please select a type of property.", "danger")
                    return  render_template('property.html', form = form)
                print("HELLO")
                img = form.media.data
                print("NAME:{}".format(img))
                filename = secure_filename(img.filename)
                if (is_picture(filename)):
                    savepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    print("\nSAVEPATH: {}\n".format(savepath))
                    img.save(savepath)
                if (not(is_picture(filename))):
                    flash("Please only upload images in the photo section.", "danger")
                    return  render_template('property.html', form = form)
                try:
                    prop = Property(title = form.title.data, no_bath=form.no_bath.data, no_bed=form.no_bed.data, location = form.location.data,\
                                    price= form.price.data, typ = form.typ.data, desc = form.desc.data, media_addr=savepath[4:])
                    flash("Property has been added successfully!", 'success')
                except Exception as e:
                    print("ERROR ERROR: \n\n{}\n\n".format(e))
                    flash("Something went wrong..., try again later.", "danger")
                return redirect(url_for('home'))
            else:
                flash("Something went wrong, please try again.", "danger")
                return  render_template('property.html', form = form)

@app.route("/uploads/<filename>")
def get_file(filename: str):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.route("/properties/")
def view_properties():
    sql = "Select * from properties;"
    try:
        print("helloooooo")
        properties = query(sql).fetchall()
        print("byeeeeeeee")
        return render_template('view_properties.html', properties = properties)
    except Exception as e:
        print("\nERRO ERROR:{}\n".format(e))
        flash("No properties currently listed.", "danger")
        properties = []
        return render_template('view_properties.html', properties = properties)

@app.route("/property/<property_id>")
def view_property(property_id):
    sql = "select * from properties where prop_id={};".format(property_id)
    try:
        prop = query(sql).fetchone()
        return render_template('view_property.html', prop = prop)
    except Exception as e:
        print("ERROR\n{}\nERROR".format(e))
        flash("This property does not exist.", "danger")
        return redirect(url_for('home'))




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
