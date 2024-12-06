import os
import argparse
from pytube import YouTube
from moviepy.editor import *

def download_youtube_media(url, output_type='mp4', output_path='.'):
    """
    Download YouTube video or audio based on specified type.
    
    :param url: YouTube video URL
    :param output_type: 'mp4' for video or 'mp3' for audio
    :param output_path: Directory to save the downloaded file
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Create YouTube object
        yt = YouTube(url)
        
        # Print video details
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        
        if output_type.lower() == 'mp4':
            # Get the highest resolution video stream
            video_stream = yt.streams.get_highest_resolution()
            
            # Download video
            print("Downloading video...")
            output_file = video_stream.download(output_path)
            print(f"Video downloaded to: {output_file}")
        
        elif output_type.lower() == 'mp3':
            # Download video first
            video_stream = yt.streams.get_highest_resolution()
            video_file = video_stream.download(output_path)
            
            # Convert to MP3
            print("Converting to MP3...")
            video_clip = VideoFileClip(video_file)
            audio_clip = video_clip.audio
            
            # Generate MP3 filename (replace video extension with .mp3)
            mp3_filename = os.path.splitext(video_file)[0] + '.mp3'
            audio_clip.write_audiofile(mp3_filename)
            
            # Close clips
            audio_clip.close()
            video_clip.close()
            
            # Remove original video file
            os.remove(video_file)
            
            print(f"Audio downloaded to: {mp3_filename}")
        
        else:
            raise ValueError("Output type must be 'mp4' or 'mp3'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Download YouTube videos or audio')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('-t', '--type', 
                        choices=['mp4', 'mp3'], 
                        default='mp4', 
                        help='Output file type (default: mp4)')
    parser.add_argument('-o', '--output', 
                        default='.', 
                        help='Output directory (default: current directory)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call download function
    download_youtube_media(args.url, args.type, args.output)

if __name__ == '__main__':
    main()