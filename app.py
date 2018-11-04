from flask import Flask, request, render_template
from json_util import getPlans
from mapping import preprocess_sql, traverse_sql

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    exec_plan = request.form['execPlanTextBox']
    sql_query = request.form['sqlTextBox']
    query_plan_dict = getPlans(exec_plan)
    do_mapping(sql_query, query_plan_dict)
    #preprocess_sql(sql_query)


def do_mapping(sql_query, query_plan_dict):
    for k,v in query_plan_dict.items():
        traverse_sql(sql_query, v)
    print(query_plan_dict)



if __name__ == '__main__':
    app.run()

