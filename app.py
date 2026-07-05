from flask import Flask, render_template, request, redirect, url_for
import PyPDF2
import os
import google.generativeai as genai
app = Flask(__name__)

# Configure Gemini
genai.configure(api_key="YOUR-API-KEY")

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

uploaded_text = ""
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

@app.route("/upload", methods=["POST"])
def upload():

    global uploaded_text

    pdf = request.files["paper"]

    # Save PDF in uploads folder
    pdf_path = os.path.join("uploads", "paper.pdf")
    pdf.save(pdf_path)

    # Read PDF from uploads folder
    reader = PyPDF2.PdfReader(pdf_path)

    uploaded_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            uploaded_text += text

    return redirect(url_for("summary"))
# ----------------------------
# Summary
# ----------------------------
@app.route("/summary")
def summary():

    global uploaded_text

    if uploaded_text == "":
        return "Please upload a PDF first."

    response = model.generate_content(
        f"""
        Summarize this research paper in simple language.

        {uploaded_text}
        """
    )

    return render_template(
        "summary.html",
        summary=response.text
    )

# ----------------------------
# Insights
# ----------------------------
@app.route("/insights")
def insights():

    global uploaded_text

    response = model.generate_content(f"""
Give important insights from this paper.

Include:

Main contribution

Strengths

Weaknesses

Future scope

Real-world applications

Research Paper:
{uploaded_text}
""")

    return render_template(
        "insights.html",
        insights=response.text
    )

# ----------------------------
# Flashcards
# ----------------------------
@app.route("/flashcards")
def flashcards():

    global uploaded_text

    response = model.generate_content(f"""
Create 10 flashcards from this research paper.

Format:

Q: Question

A: Answer

Research Paper:
{uploaded_text}
""")

    return render_template(
        "flashcards.html",
        flashcards=response.text
    )


# ----------------------------
# Quiz
# ----------------------------
@app.route("/quiz")
def quiz():

    global uploaded_text

    response = model.generate_content(f"""
Create 10 multiple choice questions.

Each question should have:

Question

A)

B)

C)

D)

Correct Answer

Research Paper:
{uploaded_text}
""")

    return render_template(
        "quiz.html",
        quiz=response.text
    )

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

    global uploaded_text

    response = model.generate_content(f"""
Extract the 20 most important keywords.

For each keyword give one-line meaning.

Research Paper:
{uploaded_text}
""")

    return render_template(
        "keywords.html",
        keywords=response.text
    )


# ----------------------------
# Explain Simply
# ----------------------------
@app.route("/explain")
def explain():

    global uploaded_text

    response = model.generate_content(f"""
Explain this research paper as if teaching a beginner.

Use simple English.

Research Paper:
{uploaded_text}
""")

    return render_template(
        "explain.html",
        explanation=response.text
    )


# ----------------------------
# Gemini AI Test
# ----------------------------
@app.route("/test-ai")
def test_ai():
    response = model.generate_content(
        "Say hello to my Research Paper Simplifier project in one sentence."
    )
    return response.text


# ----------------------------
# Run Application
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)