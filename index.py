"""
YouTube Video to MP3 Converter

This script takes a YouTube video URL as input and converts it to an MP3 file.
It uses the RapidAPI YouTube-MP36 API to fetch the video metadata and download link.

Example usage:

    $ python youtube_mp3_converter.py
    Enter Your Link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Converting...
    DONE YOUR DATA:
    Title: Rick Astley - Never Gonna Give You Up (Official Music Video)
    Duration: 03:33
    Download Link: https://example.com/download.mp3
"""

import requests
import urllib.parse

def get_video_id(link):
    """
    Extract the video ID from a YouTube URL

    Args:
        link (str): The YouTube URL

    Returns:
        str: The video ID, or None if the URL is invalid

    Example:
        >>> get_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        "dQw4w9WgXcQ"
    """
    if "youtube.com" in link:
        parsed_url = urllib.parse.urlparse(link)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        if "v" in query_params:
            return query_params["v"][0]
        else:
            print("Invalid YouTube URL. Could not extract video ID.")
    else:
        print("Invalid YouTube URL. Please enter a valid YouTube URL.")
    return None

def convert_video_to_mp3(video_id):
    """
    Convert a YouTube video to MP3 using the RapidAPI YouTube-MP36 API

    Args:
        video_id (str): The video ID

    Returns:
        dict: The video metadata and download link, or an error message if the API call fails

    Example:
        >>> convert_video_to_mp3("dQw4w9WgXcQ")
        {
            "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
            "duration": 213,
            "link": "https://example.com/download.mp3"
        }
    """
    url = "https://youtube-mp36.p.rapidapi.com/dl"
    querystring = {"id": video_id}

    headers = {
        "x-rapidapi-key": "a5494d3184msh22c0dcd2a596ab7p159360jsn3d0e74734b6f",
        "x-rapidapi-host": "youtube-mp36.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        return {"error": "API call failed", "status_code": response.status_code}
    else:
        return response.json()

def main():
    """
    Main entry point of the script
    """
    print("Youtube Video To Mp3 Convertor.\n")
    link = input("Enter Your Link: ")

    print("Converting...")
    video_id = get_video_id(link)

    if video_id:
        data = convert_video_to_mp3(video_id)

        if "error" in data:
            print(f"Error Occured: {data['error']}")
        else:
            print("DONE YOUR DATA:\n")
            duration_seconds = int(data['duration'])
            minutes, seconds = divmod(duration_seconds, 60)
            print(f"Title: {data['title']}")
            print(f"Duration: {minutes:02d}:{seconds:02d}")
            print(f"Download Link: {data['link']}")

if __name__ == "__main__":
    main()