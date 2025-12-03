from flask import render_template

def open_page_routes(app):
    @app.route('/my-top-movies/login')
    def show_login_page():
        return render_template('login-page.html')

    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/my-top-movies/create-new-user-page')
    def show_create_new_user_page():
        return render_template('create-new-user-page.html')