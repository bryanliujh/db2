from flask import Flask, request, render_template
from json_util import getPlans
from mapping import preprocess_sql

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    exec_plan = request.form['execPlanTextBox']
    sql_query = request.form['sqlTextBox']
    #getPlans(exec_plan)
    preprocess_sql(sql_query)






if __name__ == '__main__':
    app.run()

