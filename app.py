import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from textblob import TextBlob

# 1. Page Configuration & Spotify-like Dark Theme CSS
st.set_page_config(page_title="Moodify", page_icon="🎵", layout="centered")

# Injecting Custom CSS to mimic Spotify's UI
st.markdown("""
    <style>
    /* Main app background and text color */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    
    /* Input field styling */
    .stTextInput input {
        background-color: #242424 !important;
        color: #FFFFFF !important;
        border: 1px solid #3E3E3E !important;
        border-radius: 50px !important;
        padding-left: 20px !important;
    }
    
    /* Green Spotify button styling */
    .stButton>button {
        background-color: #1DB954 !important;
        color: #FFFFFF !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 10px 25px !important;
        font-weight: bold !important;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.04);
        background-color: #1ED760 !important;
    }
    
    /* Custom Card container for songs */
    .song-card {
        background-color: #181818;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        border: 1px solid #282828;
        transition: background-color 0.3s;
    }
    .song-card:hover {
        background-color: #282828;
    }
    
    /* Text styling inside cards */
    .song-title {
        color: #FFFFFF !important;
        font-size: 18px !important;
        font-weight: bold;
        text-decoration: none;
    }
    .song-title:hover {
        text-decoration: underline;
    }
    .artist-name {
        color: #B3B3B3;
        font-size: 14px;
        margin-top: 4px;
    }
    </style>
""", unsafe_allowed_html=True)

# 2. Spotify API Setup
CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
CLIENT_SECRET = "YOUR_SPOTIFY_CLIENT_SECRET"

try:
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
except Exception as e:
    st.error("Spotify Connection Error. Check your Client ID and Secret.")

# 3. Header UI
st.markdown("<h1 style='color: #1DB954; text-align: center;'>🎵 Moodify</h1>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #B3B3B3;'>Your mood determines the soundtrack.</p>", unsafe_allowed_html=True)
st.write("---")

# 4. Input Area
user_input = st.text_input("", placeholder="How are you feeling right now?")

# Center the button using Streamlit columns
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    submit_button = st.button("Get Tracks")

# 5. Logic Execution
if submit_button:
    if user_input.strip() == "":
        st.warning("Please enter your mood first!")
    else:
        # Sentiment Analysis
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity
        
        if polarity < -0.1:
            target_valence, target_energy = 0.2, 0.3
            seed_genres = ['acoustic', 'sad', 'rainy-day']
            status_msg = "💎 Playing something reflective and deep..."
        elif polarity > 0.1:
            target_valence, target_energy = 0.8, 0.8
            seed_genres = ['pop', 'dance', 'happy']
            status_msg = "🔥 Boosting the vibes with high energy!"
        else:
            target_valence, target_energy = 0.5, 0.4
            seed_genres = ['ambient', 'chill', 'lo-fi']
            status_msg = "☕ Keeping it completely relaxed..."
            
        st.markdown(f"<p style='color: #1DB954; font-weight: bold;'>{status_msg}</p>", unsafe_allowed_html=True)
        
        # Fetching data from Spotify
        try:
            results = sp.recommendations(seed_genres=seed_genres, target_valence=target_valence, target_energy=target_energy, limit=5)
            
            st.write("") # Spacer
            
            # Rendering Spotify-Style Custom HTML Cards
            for track in results['tracks']:
                track_name = track['name']
                artist_name = track['artists'][0]['name']
                track_url = track['external_urls']['spotify']
                album_cover = track['album']['images'][0]['url'] if track['album']['images'] else "https://via.placeholder.com/80"
                
                # HTML template mimicking Spotify track rows
                card_html = f"""
                <div class="song-card">
                    <img src="{album_cover}" width="65" height="65" style="border-radius: 4px; margin-right: 20px;">
                    <div>
                        <a href="{track_url}" target="_blank" class="song-title">{track_name}</a>
                        <div class="artist-name">{artist_name}</div>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allowed_html=True)
                
        except Exception as e:
            st.error(f"Error fetching music data: {e}")
