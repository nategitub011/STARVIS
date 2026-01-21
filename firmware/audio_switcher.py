# TARVIS Voice Mode Controller
# Logic: Switches between Public (Speakers) and Private (Headset)

import os

def set_tarvis_mode(mode):
    if mode == "private":
        print("TARVIS: Initiating Private Mode. Routing audio to headset...")
        # This command tells the Pi's audio system to use the USB Mic/Headset
        # os.system("pactl set-default-sink alsa_output.usb-headset")
    elif mode == "public":
        print("TARVIS: Initiating Public Mode. Broadcasting to room...")
        # This command routes audio to the screen/speakers
        # os.system("pactl set-default-sink alsa_output.platform-hdmi")
    else:
        print("Error: Unknown Mode")

# Dummy test
set_tarvis_mode("private")
