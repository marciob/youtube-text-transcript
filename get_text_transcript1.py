from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

video_url = 'https://www.youtube.com/watch?v=Bb0J_2imRQc'
video_id = video_url.split("watch?v=")[-1]

try:
    # Fetching the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Printing the transcript
    for text in transcript:
        print(text['text'])

except NoTranscriptFound:
    print("No transcript found for this video.")
