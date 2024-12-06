import os
import argparse
import yt_dlp

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
        
        # Configuration for yt-dlp
        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
        
        # Modify options based on desired output type
        if output_type.lower() == 'mp4':
            # Specifically target full video with both audio and video
            ydl_opts.update({
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
            })
        elif output_type.lower() == 'mp3':
            # Audio-only MP3 conversion with highest quality
            ydl_opts.update({
                'format': 'bestaudio/best', # Select best quality audio
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio', # Convert to audio
                    'preferredcodec': 'mp3', # Specify MP3
                    'preferredquality': '0', # Highest quality (0-9, 0 is best)
                }],
                'audioformat': 'mp3', # Ensure MP3 format
                'postprocessor_args': [
                    '-acodec', 'libmp3lame', # Use high-quality LAME encoder
                    '-b:a', '320k' # Maximum bitrate (320 kbps)
                ],
            })
        
        # Download using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            
            print(f"Downloading: {video_title}")
            
            # Perform the download
            ydl.download([url])
        
        print(f"Download completed. File saved in {output_path}")
    
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