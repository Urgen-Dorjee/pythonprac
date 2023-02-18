from flask import Flask
app = Flask(__name__)

JOBS[
{
  id=1,
  name='Urgen Dorjee',
location='Ravangla',
rating='5'
},
{
  id=2,
  name='Kalsang Nyima',
location='San Francisco',
rating='5'
},
{
  id=3,
  name='Tenzin Norzom',
location='Albany',
rating='5'
}
]


@app.route("/")
def hello_world():
    return "<p>Hello,Urgen Dorjee</p>"


if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)
  