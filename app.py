from flask import Flask, render_template, request, Response
from utils.analyzer import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = ""
    resume_output = ""
    if request.method == "POST":
        resume_text = request.form.get("resume_text", "").strip()
        job_text = request.form.get("job_description", "").strip()

        if resume_text and job_text:
            feedback, resume_output = analyze_resume(resume_text, job_text)
        else:
            feedback = "Please paste both resume text and job description."

    return render_template("index.html", feedback=feedback, resume_output=resume_output)

@app.route("/download", methods=["POST"])
def download_resume():
    resume_output = request.form.get("resume_output", "")
    return Response(
        resume_output,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename=recreated_resume.txt"}
    )

if __name__ == "__main__":
    app.run(debug=True)
