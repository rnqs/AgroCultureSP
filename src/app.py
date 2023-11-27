from flask import Flask, request
from culture import culture
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/culture', methods=['GET', 'POST'])
def culture_season():
   if request.method == 'POST':
      culture_type = request.form['culture']
      season_type = request.form['season']
      return culture(culture_type, season_type)

   else:
      return 

if __name__ == '__main__':
   app.run(debug=True)