from flask import Flask, render_template

app = Flask(__name__)

datas = [
  { "id": 1, "name": "John", "location": "New York"}, 
  {"id": 2, "name": "Alice", "location": "London"},
  { "id": 3, "name": "Bob", "location": "Paris" },
  { "id": 4, "name": "Mary", "location": "Berlin"}
  ]


@app.route("/")
def hello_world():
  return render_template('home.html',
                         data=datas,
                         company_name="Practice Playground")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
