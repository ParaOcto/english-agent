import smtplib
from google import genai
from dotenv import load_dotenv
import schedule
import time
from string import Template
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Initialize
load_dotenv()
client = genai.Client()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")  # app password (16 ký tự)
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

today = datetime.now()
formatted_date = today.strftime("%m-%d-%Y")

def AI_Node_generating_paragraph(band_toeic_min, band_toeic_max):
    words_text = AI_Node_generating_word(band_toeic_min, band_toeic_max).text

    response_paragraph = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            f"Write a short paragraph (around 150 words) that naturally uses all of the following 10 TOEIC words: \n\n"
            f"{words_text}\n\n"
            f"After the paragraph, provide a Vietnamese translation."
        )
    )

    return words_text, response_paragraph.text

def AI_Node_generating_word(band_toeic_min, band_toeic_max):
    
    response_words = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate 10 TOEIC words for learners in band {band_toeic_min}-{band_toeic_max}"
                    f" Just the words and their meaning in Vietnamese"
                        f" And please show the topic in english of these words in the first line"
    )
    return response_words

def render_template(template_path, data):
    """Đọc và thay thế dữ liệu trong file HTML template"""
    with open(template_path, "r", encoding="utf-8") as file:
        src = Template(file.read())
        return src.safe_substitute(data)

def send_email():
    subject = f"Daily English Vocabulary - {formatted_date}"

    # Generate the vocabulary and paragraph text
    words_text, paragraph_text = AI_Node_generating_paragraph(700, 800)

    # Render HTML từ template
    html_body = render_template("email_template.html", {
        "date": formatted_date,
        "words": words_text.replace("\n", "<br>"),
        "paragraph": paragraph_text.replace("\n", "<br>")
    })

    # Tạo email
    msg = MIMEMultipart("alternative")
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error sending email:", e)



# Called job at 08:00 a.m every day
# schedule.every().day.at("08:00").do(send_email)
# schedule.every(0).seconds.do(send_email)
send_email()
# Loop for running schedule
# while True:
#     schedule.run_pending()
#     time.sleep(1)
