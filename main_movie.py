from flask import Flask, url_for, render_template, redirect ,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = ''
Bootstrap5(app)
#-----------------------------------------------------------------------#
#🟡 SQLAlchemy

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = ""
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rate: Mapped[float] = mapped_column(Float, nullable=False)
    rank: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# with app.app_context():
#     movie = Movie(title='Phone Booth',
#                       year=2002,
#                       description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#                       rate=7.4,
#                       rank=10,
#                       review='My favourite character was the caller.',
#                       img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
#
#     db.session.add(movie)
#     db.session.commit()
#-----------------------------------------------------------------------#

@app.route('/')
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.title)).scalars().all()
    return render_template('index.html', movies=movies)





























app.run(debug=True)
