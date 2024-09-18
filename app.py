from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', user_count=0, comp_count=0)

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    l = ['Rock', 'Paper', 'Scissor']
    comp_choice = random.choice(l)

    user_count = int(request.form['user_count'])
    comp_count = int(request.form['comp_count'])

    if user_choice == '1':
        u_value = 'Rock'
    elif user_choice == '2':
        u_value = 'Paper'
    elif user_choice == '3':
        u_value = 'Scissor'

    result = ""
    if ((u_value == 'Paper' and comp_choice == 'Rock') or
        (u_value == 'Rock' and comp_choice == 'Scissor') or
        (u_value == 'Scissor' and comp_choice == 'Paper')):
        user_count += 1
        result = "User Wins! Computer loses."
    elif ((comp_choice == 'Paper' and u_value == 'Rock') or
          (comp_choice == 'Rock' and u_value == 'Scissor') or
          (comp_choice == 'Scissor' and u_value == 'Paper')):
        comp_count += 1
        result = "Computer Wins! User loses."
    else:
        result = "Match Draw!"

    return render_template('index.html', user_count=user_count, comp_count=comp_count, result=result, u_value=u_value, comp_choice=comp_choice)

if __name__ == '__main__':
    app.run(debug=True)
