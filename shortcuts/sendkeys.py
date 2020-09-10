import subprocess, time
# for key codes see https://gitlab.com/cunidev/gestures/-/wikis/xdotool-list-of-key-codes
subprocess.call(["xdotool", "key", "0xff08"]) #backspace
#time.sleep(.1)
subprocess.call(["xdotool", "key", "0xff08"])
#time.sleep(.1)
subprocess.call(["xdotool", "key", "0xff08"])
#time.sleep(.1)
subprocess.call(["xdotool", "key", "0x0020"]) #space

print("done")