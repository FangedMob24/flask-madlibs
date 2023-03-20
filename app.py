from flask import Flask, request, render_template
import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    story = stories.story.prompts
    return render_template("home.html",story_prompts = story)

@app.route('/story')
def story_page():
    answer_dict = {prompt : request.args[prompt] for prompt in stories.story.prompts}
    full_story = stories.story.generate(answer_dict)
    return render_template("story.html",full_story = full_story)