import smtplib
from google import genai
from dotenv import load_dotenv
import schedule
import time
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
                        f" And please show the topic of these words in the first line"
    )
    return response_words

def send_email():
    subject = f"Daily English Vocabulary - {formatted_date}"
    
    words_text, paragraph_text = AI_Node_generating_paragraph(700, 800)

    body = f"Here are your 10 TOEIC words for today ({formatted_date}):\n\n{words_text}\n\n---\n\n{paragraph_text}"

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully!")
    except Exception as e:
        print(f"Error sending email:", e)


# Called job at 08:00 a.m every day
schedule.every().day.at("08:00").do(send_email)
# schedule.every(10).seconds.do(send_email)

# Loop for running schedule
while True:
    schedule.run_pending()
    time.sleep(1)