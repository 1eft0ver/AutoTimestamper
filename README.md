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

## Sample output
<img width="1278" alt="image" src="https://github.com/1eft0ver/AutoTimestamper/assets/18338925/c19501db-d67d-4105-a9ff-3943668a1c70">

## Why?

I used to use a GoPro Hero 8 Black as a dash cam while riding my scooter. </br>
I had flashed the Labs firmware on the GoPro to enable [the timestamp feature](https://gopro.github.io/labs/control/overlays/) on my videos, which worked quite well. </br>
However, after four years of use, I started experiencing some issues with my GoPro.</br>
</br>
First, the battery would drain even when the GoPro was switched off. </br>
I often found the battery completely dead when I was already on the road. </br>
Turning off the wireless connections, voice control, and GPS seemed to mitigate the issue somewhat, although the battery would still lose several percent of charge. </br>
However, I encountered another problem - my GoPro would randomly turn itself on. </br>
Even if the battery drain issue was resolved, the camera turning on by itself would still deplete the battery. </br>
</br>
To cope with this, I had to remove the battery when the GoPro was not in use. </br>
Unfortunately, this led to another annoyance: I had to set the date and time EVERY TIME I turned the camera on. </br>
This was very frustrating, so I decided to switch to the DJI Osmo Action 4. </br>
</br>
It took me some time to choose between the GoPro 12 and the Osmo Action 4. </br>
[DJI does not seem to plan to add the timestamp feature to its products in the foreseeable future](https://forum.dji.com/thread-255104-1-1.html), but this feature is important to me. </br>
My decisive thought was, "I can implement the feature that DJI lacks myself, but I cannot fix any of the issues my GoPro had."</br>
</br>
And here we are.</br>
