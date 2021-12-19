from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/authenticate', methods=['GET','POST'])
def post():
    name = request.form.get('firstName')
    passwrd = request.form.get('psw')
    print(name,passwrd)
    if (name == 'Anthony' and passwrd == 'Anthony123') or (name == 'James' and passwrd == 'James123') or (name == 'David' and passwrd == 'David123'):
        return render_template('postbook.html')
    elif (name == 'Admin1' and passwrd == 'admin1456') or (name == 'Admin2' and passwrd == 'admin2456'):
        return render_template('postbook.html')
    return "recived: {}".format(request.form)

if __name__ == "__main__":
    app.run(debug=True)