from huggingface_hub import InferenceClient

client = InferenceClient(token="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")

def analyze_resume(resume_text, job_text):
    try:
        response = client.chat_completion(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[
                {"role": "system", "content": "You are a helpful resume reviewer."},
                {"role": "user", "content": f"""
Compare the following resume with the job description.

Resume:
{resume_text}

Job Description:
{job_text}

Provide:
1. Missing keywords
2. Suggestions for improvement
3. Match score (0–100)
4. One-sentence summary
5. A rewritten version of the resume tailored to the job description
"""}
            ],
            max_tokens=800
        )

        # Split feedback and rewritten resume
        content = response.choices[0].message["content"]
        if "Rewritten Resume:" in content:
            parts = content.split("Rewritten Resume:")
            feedback = parts[0].strip()
            resume_output = parts[1].strip()
        else:
            feedback = content
            resume_output = ""

        return feedback, resume_output

    except Exception as e:
        return f"Error during analysis: {str(e)}", ""