from flask import Flask
app = Flask("First App")

@app.route('/')
def index ():
	return "Yes it's working."

if __name__=="__main__":
	app.run()

