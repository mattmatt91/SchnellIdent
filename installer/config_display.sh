#!/bin/bash

# Install necessary packages
echo "Installing gnome-keyring and gdm3..."
sudo apt update
sudo apt install -y gnome-keyring gdm3 x11-xserver-utils

# Set up GDM3 as the default display manager
echo "Configuring GDM3 as the default display manager..."
sudo dpkg-reconfigure gdm3

# Configure display settings for GDM3 (e.g., rotation and resolution)
echo "Setting up display rotation and resolution..."
DISPLAY_SCRIPT_PATH="/usr/share/gdm/greeter/autostart/display-settings.sh"
DISPLAY_DESKTOP_PATH="/usr/share/gdm/greeter/autostart/display-settings.desktop"

# Remove any existing display configuration scripts to avoid duplicates
sudo rm -f $DISPLAY_SCRIPT_PATH $DISPLAY_DESKTOP_PATH

# Create and write the display settings script with desired rotation and resolution
sudo mkdir -p /usr/share/gdm/greeter/autostart
sudo bash -c "cat > $DISPLAY_SCRIPT_PATH" <<EOL
#!/bin/bash
# Set the desired rotation and resolution
xrandr --output HDMI-1 --rotate right --mode 1024x600 --rate 60
EOL

# Make the display settings script executable
sudo chmod +x $DISPLAY_SCRIPT_PATH

# Create the .desktop file to autostart the display settings in GDM3
sudo bash -c "cat > $DISPLAY_DESKTOP_PATH" <<EOL
[Desktop Entry]
Type=Application
Name=Display Settings
Exec=$DISPLAY_SCRIPT_PATH
X-GNOME-Autostart-enabled=true
EOL

# Configure touchscreen calibration for GDM3
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

# Restart GDM3 to apply changes
echo "Restarting GDM3 to apply display and touchscreen settings..."
sudo systemctl restart gdm3

echo "Setup complete! GDM3 is now configured with display and touchscreen settings."
