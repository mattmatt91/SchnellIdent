#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install necessary packages if not already installed
echo "Installing gnome-keyring, gdm3, and x11-xserver-utils..."
# Uncomment the following lines if the packages are not already installed
# sudo apt update
# sudo apt install -y gnome-keyring gdm3 x11-xserver-utils

# Configure GDM3 as the default display manager non-interactively
echo "Setting GDM3 as the default display manager..."
echo "gdm3 shared/default-x-display-manager select gdm3" | sudo debconf-set-selections
sudo DEBIAN_FRONTEND=noninteractive dpkg-reconfigure gdm3

# Detect display name using xrandr (only if DISPLAY is accessible)
export DISPLAY=:0
DISPLAY_NAME=$(xrandr | grep " connected" | awk '{ print $1 }' || echo "HDMI-1")
echo "Detected display: $DISPLAY_NAME"

# Configure persistent display rotation and resolution in /boot/config.txt
echo "Setting persistent display rotation and resolution in /boot/config.txt..."
BOOT_CONFIG="/boot/firmware/config.txt"

# Remove existing display configuration lines
sudo sed -i '/^hdmi_group/d;/^hdmi_mode/d;/^hdmi_cvt/d;/^display_hdmi_rotate/d' $BOOT_CONFIG

# Add custom display settings to /boot/config.txt
sudo bash -c "cat >> $BOOT_CONFIG" <<EOL

# Custom display settings
hdmi_group=2             # Use DMT mode
hdmi_mode=87             # Enable custom resolution
hdmi_cvt 1024 600 60 6   # Set resolution to 1024x600 at 60Hz
display_hdmi_rotate=3    # Rotate display to the left (90° counterclockwise)
EOL

# Configure touchscreen calibration for ADS7846 touchscreen
echo "Configuring touchscreen calibration..."
TOUCHSCREEN_CONFIG_PATH="/etc/X11/xorg.conf.d/99-calibration.conf"

# Remove any existing touchscreen calibration configuration
sudo rm -f $TOUCHSCREEN_CONFIG_PATH

# Write the new touchscreen calibration settings
sudo mkdir -p /etc/X11/xorg.conf.d
sudo bash -c "cat > $TOUCHSCREEN_CONFIG_PATH" <<EOL
Section "InputClass"
    Identifier "calibration"
    MatchProduct "ADS7846 Touchscreen"
    Option "Calibration" "59 3985 3882 172"
    Option "SwapAxes" "1"
    Driver "evdev"
EndSection
EOL


#remove pwd
sudo passwd -d si


# Prompt for a reboot to apply display and touchscreen settings
echo "Setup complete! Please reboot the system to apply display rotation and touchscreen calibration settings."



#!/bin/bash

# Define the path to the .xprofile file
XPROFILE_PATH="$HOME/.xprofile"

# Write the necessary commands to .xprofile
cat <<EOL > "$XPROFILE_PATH"
# Rotate the display to the left
xrandr --output HDMI-1 --rotate left

# Launch Chromium in full-screen mode with the specified URL
sleep 10
chromium-browser --start-fullscreen --app=http://localhost:3000 &
EOL

echo ".xprofile has been set up with display rotation and Chromium launch."


