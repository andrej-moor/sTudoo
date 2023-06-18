from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    site_title = {'title' : 'Home'}
    user = {'username' : 'Andy'}
    return '''
    <html>
      <head>
        <title>sTudoo | ''' + site_title['title'] + '''</title>
      </head>
      <body>
      <p>Hello ''' + user['username'] +'''!</p>
      </body>
    </html>'''