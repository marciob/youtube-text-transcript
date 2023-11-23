from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=Bb0J_2imRQc'

try:
    # Creating YouTube object
    yt = YouTube(video_url)

    # Fetching the caption track
    # Note: This gets the first caption track; you might need to adjust this for different languages or formats
    caption_track = yt.captions.get_by_language_code('en')

    if caption_track:
        # Fetching the SRT (SubRip Text) format of captions
        srt_captions = caption_track.generate_srt_captions()

        # Printing the transcript
        print(srt_captions)
    else:
        print("No captions found for this video.")

except Exception as e:
    print(f"An error occurred: {e}")
