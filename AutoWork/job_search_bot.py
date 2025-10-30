import requests
from bs4 import BeautifulSoup
import schedule
import time
import smtplib
from email.mime.text import MIMEText

# -----------------------------
# CONFIGURATION
# -----------------------------
EMAIL_SENDER = "thetempler68@gmail.com"
EMAIL_PASSWORD = "xwvo zuca yhpf aqok"  # generate app password if Gmail
EMAIL_RECEIVER = "shariershafin29@gmail.com"

SEARCH_ROLES = [
    "IT Support Specialist",
    "Help Desk Technician",
    "Remote IT Technician",
    "Data Analyst",
    "Business Analyst",
    "Customer Success Engineer",
    "Technical Account Manager"
]

SEARCH_TAGS = ["remote", "junior", "entry-level", "internship", "part-time", "seasonal"]

# Indeed URL
BASE_URL = "https://ca.indeed.com/jobs"

# LinkedIn cookie (get from browser DevTools -> Application -> Cookies -> li_at)
LINKEDIN_COOKIE = "AQEDATZoWXcFfjujAAABmOqzR2UAAAGZDr_LZU0ArKe7EUOdmAFuoP_dVgDm4OJkTTWzLMCSJb8b9f9wt_5V2nYKzlY1cB1D5VrRYdWrfeJzaqxw2vlQIAV7tIF5X2RzH61kzV_Jha8aygRTzmMAn6X6"

# -----------------------------
# HELPERS - Categorize Jobs
# -----------------------------
def categorize_job(title, job_str):
    title_lower = title.lower()
    if any(tag in title_lower for tag in ["intern", "internship", "part-time", "seasonal"]):
        return "internships", job_str
    else:
        return "entry", job_str

# -----------------------------
# INDEED SCRAPER
# -----------------------------
def scrape_indeed():
    internships, entry_jobs = [], []
    for role in SEARCH_ROLES:
        query = f"{role} {' OR '.join(SEARCH_TAGS)}"
        params = {"q": query, "l": "Canada", "sort": "date"}
        response = requests.get(BASE_URL, params=params, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        for job_card in soup.select("td.resultContent"):
            title = job_card.select_one("h2.jobTitle").get_text(strip=True)
            company = job_card.select_one("span.companyName").get_text(strip=True) if job_card.select_one("span.companyName") else "Unknown"
            location = job_card.select_one("div.companyLocation").get_text(strip=True) if job_card.select_one("div.companyLocation") else "Remote/Canada"
            link = "https://ca.indeed.com" + job_card.select_one("a")["href"]

            if any(tag.lower() in title.lower() for tag in SEARCH_TAGS):
                category, job_str = categorize_job(title, f"{title} - {company} ({location})\n{link}\n")
                if category == "internships":
                    internships.append(job_str)
                else:
                    entry_jobs.append(job_str)
    return internships, entry_jobs

# -----------------------------
# LINKEDIN SCRAPER
# -----------------------------
def scrape_linkedin():
    headers = {
        "User-Agent": "Mozilla/5.0",
        "cookie": f"li_at={LINKEDIN_COOKIE};"
    }
    internships, entry_jobs = [], []
    for role in SEARCH_ROLES:
        query = f"{role} {' OR '.join(SEARCH_TAGS)}"
        url = f"https://www.linkedin.com/jobs/search/?keywords={query}&location=Canada&f_TPR=r86400&f_WT=2&f_JT=I"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for job_card in soup.select("div.base-card"):
            title = job_card.select_one("h3.base-search-card__title").get_text(strip=True)
            company = job_card.select_one("h4.base-search-card__subtitle").get_text(strip=True)
            link = job_card.select_one("a.base-card__full-link")["href"]

            if any(tag.lower() in title.lower() for tag in SEARCH_TAGS):
                category, job_str = categorize_job(title, f"{title} - {company}\n{link}\n")
                if category == "internships":
                    internships.append(job_str)
                else:
                    entry_jobs.append(job_str)
    return internships, entry_jobs

# -----------------------------
# EMAIL SENDER
# -----------------------------
def send_email(internships, entry_jobs):
    if not internships and not entry_jobs:
        body = "No new jobs found today."
    else:
        body = ""
        if internships:
            body += "🎓 INTERNSHIPS / PART-TIME:\n" + "\n".join(internships) + "\n\n"
        if entry_jobs:
            body += "💼 ENTRY-LEVEL / JUNIOR FULL-TIME:\n" + "\n".join(entry_jobs)

    msg = MIMEText(body)
    msg["Subject"] = "📩 Daily Job Digest - Remote & Entry-Level Roles"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

    print("✅ Email sent!")

# -----------------------------
# MAIN JOB TASK
# -----------------------------
def job_task():
    print("🔍 Running daily job search...")
    indeed_intern, indeed_entry = scrape_indeed()
    linkedin_intern, linkedin_entry = scrape_linkedin()

    all_internships = indeed_intern + linkedin_intern
    all_entry_jobs = indeed_entry + linkedin_entry

    send_email(all_internships, all_entry_jobs)

# -----------------------------
# SCHEDULER
# -----------------------------
schedule.every().day.at("12:00").do(job_task)

print("📌 Job search automation started. Waiting for 12:00 daily...")
while True:
    schedule.run_pending()
    time.sleep(60)