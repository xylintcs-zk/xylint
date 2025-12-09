from flask import Flask, render_template, request, session
from flask_session import Session
from config import Config
from commands import process_command, CLEAR_COMMAND

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

@app.errorhandler(404)
def not_found(e):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('error/500.html'), 500

@app.route('/')
def index():
    if "chat_history" not in session:
        session["chat_history"] = []
    return render_template("index.html", chat_history=session["chat_history"])

@app.route('/command', methods=['POST'])
def command():
    cmd = request.form.get('cmd').strip()

    # handle clear chat
    if cmd.lower() == CLEAR_COMMAND:
        session["chat_history"] = []
        session.modified = True
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return "CLEAR"
        else:
            return render_template("index.html", chat_history=session["chat_history"])

    # handle other commands
    response = process_command(cmd)

    # save to chat history
    if "chat_history" not in session:
        session["chat_history"] = []
    session["chat_history"].append(("user", cmd))
    session["chat_history"].append(("bot", response))
    session.modified = True

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return response
    else:
        return render_template("index.html", chat_history=session["chat_history"])

if __name__ == "__main__":
    app.run()
