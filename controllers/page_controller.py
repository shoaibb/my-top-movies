def open_page_routes(app):
    @app.route('/')
    def show_login_page():
        return "Login Page."

    @app.route('/home')
    def home():
        return "Home Page."

    @app.route('/about')
    def about():
        return "About Page."