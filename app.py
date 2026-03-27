from flask import Flask, render_template

# Templates live at repo root (index.html, pages/...). Static assets (css/, img/, lib/, js/) are served from root too.
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

@app.route('/404')
def error_404():
    return render_template('pages/404.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/admin-login')
def admin_login():
    return render_template('pages/admin-login.html')

@app.route('/appointment')
def appointment():
    return render_template('pages/appointment.html')

@app.route('/call-to-action')
def call_to_action():
    return render_template('pages/call-to-action.html')

@app.route('/client')
def client():
    return render_template('pages/client.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/facility')
def facility():
    return render_template('pages/facility.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('pages/login.html')

@app.route('/medicine')
def medicine():
    return render_template('pages/medicine.html')

@app.route('/services')
def services():
    return render_template('pages/services.html')

@app.route('/team')
def team():
    return render_template('pages/team.html')

@app.route('/testimonial')
def testimonial():
    return render_template('pages/testimonial.html')

@app.route('/underWork')
def under_work():
    return render_template('pages/underWork.html')

if __name__ == '__main__':
    app.run(debug=True)
