from youtube_transcript_api import YouTubeTranscriptApi
import json
import csv
import pandas as pd



video_id = "orlUDdeoxZQ"

def data_source_transscripts(video_id):
    return pd.DataFrame(YouTubeTranscriptApi.get_transcript(video_id))

def video_id_collector(url):
    return url.split("v=")[1].split("&t=")[0]

def save_transcripts(video_id, filename):
    df_to_save = data_source_transscripts(video_id)
    df_to_save.to_csv(f"{filename}.csv")


url_list  = ["https://www.youtube.com/watch?v=0oAJsPFH2wk", ]
for url in url_list:
    save_transcripts(video_id_collector(url))




