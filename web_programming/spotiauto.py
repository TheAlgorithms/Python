import subprocess
import sys
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)

def get_mood() -> Optional[str]:
    """
    Display a pop-up dialog to ask the user for their mood (happy, sad, etc.).
    Returns the mood as a string or None if the user cancels.
    """
    script = '''
    set mood to choose from list {"Happy", "Sad", "Chill", "Energetic"} with prompt "How are you feeling today?"
    if mood is false then return "None" -- If the user cancels, return "None"
    return item 1 of mood
    '''
    try:
        mood = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True).stdout.strip()
        return mood if mood != "None" else None
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in getting mood: {e}")
        return None

def get_shuffle_preference() -> bool:
    """
    Ask the user if they want to enable shuffle mode.
    Returns True if they choose "Yes", False otherwise.
    """
    script = '''
    set shuffle_pref to choose from list {"Yes", "No"} with prompt "Do you want shuffle mode enabled?"
    if shuffle_pref is false then return "No" -- Default to "No" if user cancels
    return item 1 of shuffle_pref
    '''
    try:
        shuffle_response = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True).stdout.strip()
        return shuffle_response == "Yes"
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in getting shuffle preference: {e}")
        return False  # Default to shuffle off in case of error

def check_spotify_running() -> bool:
    """
    Check if the Spotify application is currently running.
    Returns True if Spotify is running, False otherwise.
    """
    script = 'tell application "System Events" to (name of processes) contains "Spotify"'
    try:
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True).stdout.strip()
        return result == 'true'
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking Spotify running status: {e}")
        return False

def offer_to_open_spotify() -> bool:
    """
    Ask the user if they want to open Spotify if it's not running.
    Returns True if the user wants to open Spotify, False otherwise.
    """
    script = '''
    display dialog "Spotify is not running. Do you want to open it?" buttons {"Yes", "No"} default button "Yes"
    set user_choice to button returned of result
    return user_choice
    '''
    try:
        user_choice = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True).stdout.strip()
        return user_choice == "Yes"
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in getting user's choice to open Spotify: {e}")
        return False

def open_spotify() -> None:
    """
    Open the Spotify application.
    """
    try:
        subprocess.run(['open', '-a', 'Spotify'], check=True)
        logging.info("Spotify is now opening...")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to open Spotify: {e}")
        sys.exit(1)

def control_spotify(command: str) -> None:
    """
    Use AppleScript to control the Spotify desktop app on macOS.
    """
    script = f'tell application "Spotify" to {command}'
    try:
        subprocess.run(['osascript', '-e', script], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to send command to Spotify: {e}")
        sys.exit(1)

def set_spotify_volume(volume: int) -> None:
    """
    Set the volume level for Spotify.
    """
    control_spotify(f'set sound volume to {volume}')

def play_playlist(playlist_uri: str, shuffle: bool) -> None:
    """
    Play a specific playlist on Spotify based on its URI, with the option to enable shuffle.
    """
    control_spotify(f'set shuffling to {str(shuffle).lower()}')  # Enable or disable shuffle
    control_spotify(f'play track "{playlist_uri}"')  # Play the playlist

def get_volume_for_mood(mood: str) -> int:
    """
    Get the volume level based on the user's mood.
    """
    volume_levels = {
        "Happy": 70,
        "Sad": 60,
        "Chill": 50,
        "Energetic": 100
    }
    return volume_levels.get(mood, 50)  # Default to 50 if mood is not found

def get_current_track() -> Optional[str]:
    """
    Retrieve the currently playing track's name, artist, and album in Spotify.
    Returns a formatted string with the track information, or None if no track is playing.
    """
    script = '''
    tell application "Spotify"
        if player state is playing then
            set track_name to name of current track
            set track_artist to artist of current track
            set track_album to album of current track
            return track_name & " by " & track_artist & " from the album " & track_album
        else
            return "No track is currently playing."
        end if
    end tell
    '''
    try:
        track_info = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True).stdout.strip()
        return track_info if track_info else None
    except subprocess.CalledProcessError as e:
        logging.error(f"Error retrieving current track: {e}")
        return None

def validate_mood_and_play_playlist(mood: Optional[str], mood_playlists: dict) -> None:
    """
    Validate the mood and play the corresponding playlist.
    Set shuffle mode and adjust the volume based on the user's preferences and mood.
    Display the currently playing track.
    """
    if mood:
        playlist_uri = mood_playlists.get(mood)
        if playlist_uri:
            logging.info(f"Playing {mood} playlist...")

            # Check if Spotify is running
            if not check_spotify_running():
                logging.warning("Spotify is not running.")
                if offer_to_open_spotify():
                    open_spotify()
                else:
                    logging.info("Spotify is not opened. Exiting.")
                    sys.exit(0)

            # Get the shuffle preference
            shuffle = get_shuffle_preference()

            # Get the volume level based on the mood
            volume = get_volume_for_mood(mood)
            logging.info(f"Setting volume to {volume} for mood {mood}")
            set_spotify_volume(volume)

            # Play the playlist with the appropriate shuffle setting
            play_playlist(playlist_uri, shuffle)

            # Get and display the currently playing track
            track_info = get_current_track()
            if track_info:
                logging.info(f"Currently playing: {track_info}")
            else:
                logging.warning("No track is currently playing.")
        else:
            logging.warning(f"No playlist found for mood: {mood}")
    else:
        logging.info("No mood selected. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    # Define playlists for each mood
    mood_playlists = {
        "Happy": "spotify:playlist:37i9dQZF1DXdPec7aLTmlC",  # Replace with your playlist URI
        "Sad": "spotify:playlist:37i9dQZF1DWVrtsSlLKzro",    # Replace with your playlist URI
        "Chill": "spotify:playlist:37i9dQZF1DX4WYpdgoIcn6",  # Replace with your playlist URI
        "Energetic": "spotify:playlist:37i9dQZF1DX76Wlfdnj7AP" # Replace with your playlist URI
    }

    # Get the user's mood
    user_mood = get_mood()

    # Validate mood and play the corresponding playlist
    validate_mood_and_play_playlist(user_mood, mood_playlists)
