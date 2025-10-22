from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

@app.route('/')
# გამოგვაქვს მთავარი გვერდი
def index():
    return render_template('index.html')

@app.route('/multiply/<int:num1>/<int:num2>/<int:num3>/<int:num4>')
# გავამრავლოთ ოთხი რიცხვი
def multiply_numbers(num1, num2, num3, num4):
    result = num1 * num2 * num3 * num4
    message = f"{num1} * {num2} * {num3} * {num4} = {result}"
    return render_template('result.html', message=message)

@app.route('/json')
# გამოვიტანოთ Json
def show_json():
    data = {
        'project_name': 'მარტივი Flask აპლიკაცია',
        'author': 'მე, ჩემი კაცობა და ჩემი მეობა',
        'status': 'გამოქვეყნებული',
        'version': '1.0'
    }
    json_string = json.dumps(data, ensure_ascii=False, indent=4)
    return render_template('json.html', message=json_string)

# 4. მომხმარებლის მისალმების route
@app.route('/name/<string:name>')
# მივესალმოთ მომხმარებელს
def greet_user(name):
    message = f"მოგესალმები, {name}!"
    return render_template('greeting.html', message=message)

@app.errorhandler(404)
# დავამუშავოთ შეცდომები
def page_not_found(e):
    message = "გარემოებების უცნაური დამთხვევის გამო, თქვენ მოხვდით არარსებულ გვერდზე."
    return render_template('404.html', message=message), 404

if __name__ == '__main__':
    app.run(debug=True)