# AutoTimestamper
A Python script to add a ticking timestamp to a video, calculated by the media created time and the duration of the video file.

## Prerequisites
- [Python 3](https://www.python.org/downloads/)
- [ImageMagick](https://imagemagick.org/index.php)
- pip install -r .\requirements.txt

## Usage
```powershell
python add_timestamp_to_video.py <video_file_path>
```

## Why?

I used to use GoPro Hero 8 Black as the dash cam while riding my scooter. </br>
I flashed the Labs firmware to my GoPro so that I can leverage [this feature](https://gopro.github.io/labs/control/overlays/) to burn the timestamp on the videos I shot on the GoPro. </br>
It worked pretty well. </br>
However, after the 4-year period of usage, I started to run into some issues with my GoPro.</br>
</br>
First, the battery drains even when the GoPro was switched off. </br>
I always found that my GoPro is out of battery when I was already on the road. </br>
Turning off the wireless connections, voice control, and GPS seems to fix the issue (sort of, it still lost several percent of battery but at least it's not completely dead). </br>
BUT here's another issue I ran into - my GoPro randomly turn itself on. </br>
So even if the draining battery issue is resolved, there's still a chance that my GoPro turns itself on and resulting in the drained battery.</br>
I had no choice but to take out the battery when the GoPro was not in use, but guess what - my GoPro started to ask me to set the date and time **EVERY TIME** I turn it on. </br>
I was pretty pissed off at this point, so I switched to the DJI Osmo Action 4. </br>
</br>
It actually took me some time to choose between the GoPro 12 or the Action 4. </br>
[DJI does not seem to add the timestamp feature to its product in the foreseeable future](https://forum.dji.com/thread-255104-1-1.html), but this feature is quite important to me.</br>
The decisive thought that came into my mind was that "I can implement the feature that DJI does not have myself, but I cannot fix any of the issues my GoPro had". </br>
</br>
So here we are. </br>
</br>