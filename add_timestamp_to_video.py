import os
import sys
import pytz
import datetime
import pythoncom
from win32comext.propsys import propsys, pscon
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\convert.exe')
file_path = os.path.abspath(sys.argv[1])
folder, filename = os.path.split(file_path)
clip = VideoFileClip(file_path)

# Get and calculate the timestamp start time
# If media created time is valid, use this value
# If there's no media created time, use (file created time - clip duration) instead
pythoncom.CoInitialize()
properties = propsys.SHGetPropertyStoreFromParsingName(file_path)
dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
if dt is None:
    dt = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
    dt -= datetime.timedelta(0, clip.duration)
elif not isinstance(dt, datetime.datetime):
    dt = datetime.datetime.fromtimestamp(int(dt))
    dt = dt.replace(tzinfo=pytz.timezone('UTC'))
else:
    dt = dt.astimezone(pytz.timezone('Asia/Taipei'))
dt_start = dt
print("Media created time: " + str(dt_start))
pythoncom.CoUninitialize()

#Split the clip into 1-second segments then add the corresponding timestamp to each segments
cliplist = [clip]
dt_current = dt_start
dt_end = dt_start + datetime.timedelta(0, int(clip.duration))
segment_start = 0
while True:
    print("Processing clip at: " + dt_current.strftime("%Y/%m/%d %H:%M:%S"))
    segment = TextClip(dt_current.strftime("%Y/%m/%d %H:%M:%S"), font="msjh.ttc", fontsize=50.0, color="white", bg_color="transparent", stroke_color="black", stroke_width=2.0)
    segment = segment.set_position((0.8, 0.95), relative=True).set_duration(1.0 if dt_current < dt_end else clip.duration - segment_start).set_start(segment_start)
    segment_start += 1
    dt_current += datetime.timedelta(0, 1)
    cliplist.append(segment)
    if dt_current > dt_end:
        break;

#Write the timestamped clip as <filename>_processed.<file_extension>
clip = CompositeVideoClip(cliplist)
output_filename = filename[:filename.rfind('.')] + "_processed" + filename[filename.rfind('.'):] 
clip.write_videofile(output_filename, threads=8, logger=None)
clip.close()