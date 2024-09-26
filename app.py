from flask import Flask, render_template, jsonify

app = Flask(__name__)
# test3
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'GuangDong',
        'salary': 'RMB. 9,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'BeiJin',
        'salary': 'RMB. 8,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer ',
        'location': 'BeiJin',
        'salary': 'RMB. 10,000'
    },
    {
        'id': 3,
        'title': 'Backend Engineer ',
        'location': 'BeiJin',
        'salary': 'RMB. 12,000'
    }
]

@app.route("/")
def hello_lwfeng():
    return render_template('home2.html',
                           jobs=JOBS,
                           company_name='lwfeng')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)