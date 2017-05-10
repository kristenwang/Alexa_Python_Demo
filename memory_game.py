import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("FindMeAnActivity")
def hello_intent():
    msg = render_template('prompt_for_activities')
    return question(msg)

@ask.intent("SelectActivityIntent", convert={'activityName': str})
def select_activities(activityName):
    session.attributes['activityName'] = activityName
    if activityName == 'movies':
        msg = render_template('prompt_for_movies', activityName=activityName)
    if activityName == 'park':
        msg = render_template('prompt_for_parks', activityName=activityName)
    if activityName == 'restaurant':
        msg = render_template('prompt_for_restaurant', activityName=activityName)
    return question(msg)

@ask.intent("PlaceIntent", convert={'place': str})
def select_activities(place):
    session.attributes['place'] = place
    msg = render_template('prompt_for_place', place=place)
    return question(msg)

@ask.intent("MovieIntent", convert={'movie': str})
def select_activities(movie):
    session.attributes['movie'] = movie
    msg = render_template('prompt_for_movie', movie=movie)
    return question(msg)

@ask.intent("TimeIntent", convert={'times': str})
def select_activities(times):
    session.attributes['times'] = times
    msg = render_template('prompt_for_time', times=times)
    return question(msg)

@ask.intent("TransportationIntent", convert={'transportation': str})
def select_activities(transportation):
    session.attributes['transportation'] = transportation
    if transportation == 'bus':
        msg = render_template('prompt_for_bus', transportation=transportation)
    if transportation == 'taxi':
        msg = render_template('prompt_for_taxi', transportation=transportation)
    if transportation == 'walk':
        msg = render_template('prompt_for_walk', transportation=transportation)
    if transportation == 'subway':
        msg = render_template('prompt_for_subway', transportation=transportation)
    return question(msg)


if __name__ == '__main__':

    app.run(debug=True)