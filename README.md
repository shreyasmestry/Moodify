# 🎵 Moodify

Moodify is a lightweight web application that reads your mind—or at least your mood—and serves up the perfect soundtrack. Powered by **Python**, **Streamlit**, and **YouTube Music**, the app analyzes the sentiment of whatever you type and immediately pulls up curated playlists to match your vibe. 

No ads, no logins, and 100% free (no premium accounts required!).

---

## 🚀 Features

* **Smarter Vibe Checking:** Uses Natural Language Processing (NLP) to detect the exact emotional tone of your text (Positive, Negative, or Neutral).
* **YouTube Music Integration:** Dynamically searches and parses community and official playlists on the fly.
* **Built-in Media Players:** Streamlit automatically embeds playable YouTube widgets right in the browser.
* **Sleek Dark UI:** Custom Spotify-inspired styling complete with reactive cards and custom inputs.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **NLP / Sentiment Analysis:** [TextBlob](https://textblob.readthedocs.io/)
* **Music API:** [ytmusicapi](https://github.com/sigma67/ytmusicapi)

---

## 💻 Local Installation & Setup

Want to run Moodify on your own machine? It takes less than two minutes.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

### 2. Install Dependencies
Make sure you have Python 3.8+ installed, then run:

Bash
pip install -r requirements.txt
### 3. Launch the App
Bash
streamlit run app.py
Your browser will automatically open to http://localhost:8501.
