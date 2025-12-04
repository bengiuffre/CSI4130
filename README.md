AI Resume Analyzer
==================

A Flask web application that helps job seekers improve their resumes by comparing them against job descriptions.  
The app provides feedback, keyword suggestions, match scores, and more based on a curated job due to AI assistance.

------------------------------------------------------------
FEATURES
------------------------------------------------------------
- Paste Resume & Job Description:.
- AI-Powered Feedback:
  * Missing keywords
  * Suggestions for improvement
  * Match score (0–100)
  * One-sentence summary

- Modern UI:
  * Centered layout
  * Large resume text area, smaller auto-expanding job description box
  * Scrollable feedback panel for long outputs
  * Styled buttons and panels with responsive design

------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------
project_root/
│
├── app.py                # Flask app entry point
├── utils/
│   └── analyzer.py       # Hugging Face integration
├── templates/
│   └── index.html        # HTML template with form and feedback panels
└── static/
    └── style.css         # Modern CSS styling

------------------------------------------------------------
SETUP INSTRUCTIONS
------------------------------------------------------------
1. Clone the repository
   
2. Use Visual studio with python installed and other depdencies which can be found in requirements.txt

3. Install dependencies
   pip install flask huggingface_hub

4. Set your Hugging Face token
   - Open utils/analyzer.py
   - Replace "hf_your_token_here" with your Hugging Face API token

5. Run the app
   python app.py
   Visit http://127.0.0.1:5000 in your browser.

------------------------------------------------------------
USAGE
------------------------------------------------------------
- Paste your resume text into the large textarea.
- Paste the job description into the smaller textarea.
- Click Analyze to receive feedback and a rewritten resume.
- Scroll through feedback if it is long.

------------------------------------------------------------
FUTURE ENHANCEMENTS
------------------------------------------------------------
- Export rewritten resume as .docx or .pdf
- Add keyword highlighting in feedback
- Support multiple job descriptions for comparison