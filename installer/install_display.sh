sudo nano /boot/firmware/config.txt # append: display_rotate=3

sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install -y xserver-xorg-input-evdev


sudo nano /boot/firmware/config.txt 
# append:
pi@raspberrypi ~ $ sudo nano /boot/config.txt
 
#LCD Display HDMI Touchscreen Waveshare 7inch 1024×600
dtparam=i2c_arm=on
dtparam=spi=on
enable_uart=1
hdmi_group=2
hdmi_mode=1
hdmi_mode=87
hdmi_cvt 1024 600 60 6 0 0 0
dtoverlay=ads7846,cs=1,penirq=25,penirq_pull=2,speed=50000,keep_vref_on=0,swapxy=0,pmax=255,xohms=150,xmin=200,xmax=3900,ymin=200,ymax=3900


sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf

Section "InputClass"
Identifier "calibration"
MatchProduct "ADS7846 Touchscreen"
Option "Calibration" "59 3985 3882 172"
Option "SwapAxes" "1"
Driver "evdev"
EndSection

sudo apt-get install -y xinput-calibrator