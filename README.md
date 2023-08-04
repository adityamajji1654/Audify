# Audify
Audify is a versatile Python project that enables you to extract audio from videos in any format. It supports various input sources, including locally uploaded video files and video links from popular platforms such as YouTube, Facebook, and Twitch streams. Audify also provides the functionality to add captions to the extracted audio.
## Features 
* Extract audio from videos in any format, including .mp4 and .mov.
* Support for uploaded video files in any video format.
* Accept video links from platforms such as YouTube, Facebook, and Twitch streams.
* User Authentication
* Add captions to the extracted audio in User-defined captions at specific timestamps.

## Libraries Installation

The following libraries need to be installed to run the code:

- Django: Use the command `pip install django`.
- Pytube: Use the command `pip install pytube`. Please note that there are small bugs in pytube related to extracting videos from YouTube links. You can refer to [this fix1](https://github.com/pytube/pytube/issues/1678) and [fix2](https://stackoverflow.com/questions/68680322/pytube-urllib-error-httperror-http-error-410-gone) for resolving the issue.
- Youtube-dl: Use the command `pip install youtube_dl`.
- Moviepy: Use the command `pip install moviepy`.
- Pydub: Use the command `pip install pydub`.
- Mutagen: Use the command `pip install mutagen`.
- FFMPEG: Refer to [this guide](https://ffmpeg.org/) for installation instructions.

Please make sure to install these libraries before running the code.




## Installation

To use Audify, follow these steps to set it up on your system:

1. Clone the repository:

   ```bash
   git clone https://github.com/sankooru14/audify.git
   cd audify
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
4. Run the migration commands to set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py makemigrations accounts
   python manage.py migrate
5. Run the Audify application
   ```bash
   python manage.py runserver

6. Access the web application through your web browser by visiting http://localhost:8000.






