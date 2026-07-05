from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ----------------------------
# Home Page
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------
# Register Page
# ----------------------------
@app.route("/register")
def register():
    return render_template("register.html")


# ----------------------------
# Login Page
# ----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))

    return render_template("login.html")


# ----------------------------
# Dashboard
# ----------------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ----------------------------
# Summary
# ----------------------------
@app.route("/summary")
def summary():
    return render_template("summary.html")


# ----------------------------
# Insights
# ----------------------------
@app.route("/insights")
def insights():
    return render_template("insights.html")


# ----------------------------
# Flashcards
# ----------------------------
@app.route("/flashcards")
def flashcards():
    return render_template("flashcards.html")


# ----------------------------
# Quiz
# ----------------------------
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


# ----------------------------
# AI Chat
# ----------------------------
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


# ----------------------------
# Keywords
# ----------------------------
@app.route("/keywords")
def keywords():
    return render_template("keywords.html")


# ----------------------------
# Explain Simply
# ----------------------------
@app.route("/explain")
def explain():
    return render_template("explain.html")


# ----------------------------
# Run Application
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)