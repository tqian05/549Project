from flask import Flask, render_template, send_from_directory, request
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_url_path='')
app.debug=True
Bootstrap(app)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/concept')
def concept():
    layman_description = "EZPZE will allow its user to use a portable trackpad on whatever solid surface they want."
    technical_description = "The prototye uses a set of piezoelectric microphones and vibration speakers to sense touch and location. " \
                            "Bluetooth is then used to transmit information that the user can use on their device."
    return render_template('concept.html', layman = layman_description, technical = technical_description)


@app.route('/components')
def component():
    components_list = ['/static/images/piezo.jpg', '/static/images/vibration.jpg', 'static/images/materials.png']
    return render_template('components.html', components_list = components_list)

@app.route('/comp')
def competition():
    competition = ["TOUCHE"]
    competition_urls = ["http://www.disneyresearch.com/project/touche-touch-and-gesture-sensing-for-the-real-world/"]
    return render_template('comp.html', competition = competition, competition_urls = competition_urls)

@app.route('/motivation')
def motivation():
    motivation = "Conventionally, a trackpad has fixed dimensions and is " \
                 "either attached to your machine or cannot be transported easily"
    solution = "Using our product, we want to create a trackpad that is easily scalable in size," \
               " has high portability and operates at low power."
    return render_template('motivation.html', motivation = motivation, solution = solution)

@app.route('/requirements')
def requirements():
    requirements = ["Human Interaction: This device must be able to take in user input as a form of " \
                   "touch on a surface and convert the signals into a language that can be " \
                   "understood by existing systems for control.",
                    "Wireless Communication: Each of the components must be able to wirelessly "
                    "communicate with one another",
                    "Low Power Operation: We want this device to be portable and to have its own rechargeable "
                    "power source for optimum user experience. In order to achieve this we need to operate "
                    "each component at relatively low power.",
                    "Intuitive Feedback: The device must have feedback to indicate the state of the system "
                    "and whether it is operating properly, especially in the necessity of calibration.",
                    "Accurate Calculation of Positioning: This is a necessity for the device to be "
                    "usable in a real system. Generally speaking, most modern devices has "
                    "thousands of pixels on the screen, so we need to achieve a certain level of "
                    "granularity in order for it to operate in a useful manner.",
                    "Compactness: In order for the device to be carried around, it needs to be "
                    "relatively small and portable. Also, we want to the device to be easily mountable "
                    "on a vertical surface such as a wall, so the sensor components must be "
                    "relatively lightweight and can be attached easily on different surfaces."]

    return render_template('requirements.html', requirements = requirements)



if __name__ == "__main__":
    app.run()