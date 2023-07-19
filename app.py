from flask import Flask, redirect, request, render_template, url_for
import random

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

chubby = {
    "https://preview.redd.it/fqv8d7ai4lcb1.jpg?width=640&crop=smart&auto=webp&s=a353520c21fde48b0931d39506b2d9e9b06e6b1d": "finn",
    "https://preview.redd.it/0l0c46m1bicb1.jpg?width=640&crop=smart&auto=webp&s=d2f0b86ca473ef11283aac98984a3b9a0122b826": "clarissa",
    "https://i.redd.it/2n34fk1atmcb1.jpg": "snowy",
    "https://preview.redd.it/ldzojjwomicb1.jpg?width=640&crop=smart&auto=webp&s=68e32334bb16be08963a35003dc8d9ad4e19638e": "meowie",
    "https://preview.redd.it/j9lgqyhnmbcb1.png?width=640&crop=smart&auto=webp&s=929d8d7325d9224dd41ab98457282369b5edecc6": "tao",
    "https://preview.redd.it/imc3p2ihw8cb1.jpg?width=640&crop=smart&auto=webp&s=d147717b8183e99c84458f48ee591a261d2fe48a": "maurice",
    "https://i.redd.it/uni792mav9cb1.jpg": "julian"
}

cats = {
    "finn": 7,
    "clarissa": 10,
    "snowy": 8,
    "meowie": 9,
    "tao": 8,
    "julian": 27
}

cart = []

def find_a(cats, a):
    for i in cats:
        if cats[i] == a:
            return i

# Your code should be below
@app.route("/")
def index():
    return render_template("home.html", chubby=chubby)

@app.route("/cats/<a>")
def cat_name(a):
    return render_template(f"cats.html", name=a, image=find_a(chubby, a), cute=cats[a])

@app.route("/cart")
def cart():
    return render_template("cart.html")

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(port=6969,debug=True)
