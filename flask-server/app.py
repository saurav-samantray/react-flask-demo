import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
	current_time = datetime.datetime.now()  
	return {'time': current_time}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)