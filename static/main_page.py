from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.debug=True
Bootstrap(app)

@app.route('/')
def hello_world():
    elevator_pitch = "pitchin"
    return render_template('index.html', elevator_pitch = elevator_pitch)

@app.route('/concept')
def concept():
    concepts = " wheee whasssupppp "
    return render_template('concept.html', concepts=concepts)

@app.route('/components')
def component():
    components_list = ["hi", "bye"]
    return render_template('components.html', components_list = components_list)

@app.route('/comp')
def competition():
    return render_template('comp.html')

@app.route('/motivation')
def motivation():
    return render_template('motivation.html')

@app.route('/requirements')
def requirements():
    return render_template('requirements.html')



if __name__ == "__main__":
    app.run()