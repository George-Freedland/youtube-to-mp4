## Youtube to mp4/mp3 python script.  

# Requirements:  
Create python virtual environment  

pip install -r requirements.txt  

brew install ffmpeg  

# Usage:  
python main.py "https://www.youtube.com/watch?v=uq-deRtvedI"  

specify output location (default same directory as code)  
python main.py "https://youtube.com/watch?v=example" -o downloads

specify file type (defalut mp4)  
python main.py "https://youtube.com/watch?v=example" -t mp3

python main.py "https://www.youtube.com/watch?v=uq-deRtvedI" -t mp4


