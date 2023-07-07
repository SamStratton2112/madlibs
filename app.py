"""Madlibs Stories."""

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

class Story:
    """Madlibs story.
x
    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/home')
def home_page():
    """Home Page"""
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story',)
def story_page():
    text = story.generate(request.args)
    # does request.args refer to all input text fields and does 
    # it create a dictionary with them that fills in the correct missing text? 
    # or is this more of a as entered type thing where all the inputs are 
    # entered into missing text fields as they were collected by initializing the story? 
    return render_template("story.html", text = text)
    # place = request.args["place"]
    # noun = request.args["noun"]
    # verb = request.args["verb"]
    # adjective = request.args["adjective"]
    # plural_noun = request.args['plural_noun']
    # return render_template('story.html', place=place, noun=noun,verb=verb,adjective=adjective,plural_noun=plural_noun)
    