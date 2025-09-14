from flask import Flask, request, render_template, jsonify
app = Flask(__name__)




jobs = [
    {
    'id':'1',
    'job title':'Software Engineer',
    'location':'juba',
    'salary':'20000'
    },
    {
    'id':'2',
    'job title':'Mechanical Engineer',
    'location':'Gumbo',
    'salary':'230000'
     },
    {
    'id':'3',
    'job title':'Civil Engineer',
    'location':'Juba Town',
    'salary':'80000'
    },
        ]

@app.route('/')
def home():
    return render_template("index.html", jobs=jobs)

@app.route("/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)