# How to organize hackathons

This is a 3 lessons training on how to organize hackathons.

Each session has it own folder for slides.
To run slides, use the [Rainbowbreeze's SelfHosted Slide Presenter](https://github.com/rainbowbreeze/slide-presenter), using the lesson folder with the -slide-dir parameter.

``` bash
# Download the slides, and the app to present them
cd slides
git clone https://github.com/rainbowbreeze/slide-presenter
git clone https://github.com/rainbowbreeze/talks-and-demoes.git

# Configure the SelfHosted Slide Present (following the instruction in the related README.md file)
cd slide-presenter
python 3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Present the first lesson of the "How to organize an hackathon" training
python app.py --slide-dir ../talks-and-demoes/2025-hackathon_training/slides_session_1
``` 

Open http://127.0.0.1:5000 in a web browser to show the slides
