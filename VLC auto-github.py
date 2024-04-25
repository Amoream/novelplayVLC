import subprocess
# Path to VLC
vlc_path = r"C:\XXX\XXX\XXX\XXX"

#Path to the video
video_file_path = r"C:\XXX\XXX\XXX\XXX"

# starts VLC with the commands assigned
command = [
    vlc_path,
    "--fullscreen",
    "--loop",
    "--no-plugins-cache",
    video_file_path,
]

try:
    # Start VLC with the modified command
    subprocess.Popen(command)
except Exception as exc:
    print("Error starting VLC:", exc)