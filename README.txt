Recommended operating system: Raspberry Pi OS

Needed software on PC (not raspberry Pi):
Blender3D to open blend file
Cura or other to make model printable
Optional: Code editor - to make some changes in code
Also some basic 3D printing knowledge

Keep in mind it would be better to use DC motor controller rather than this solution, non the less it works,
it's cheaper and gives basic understanding of how MOSFETs work. 

3D printer that was used: Ender 3 v3 SE with 0.4 nozzle
Keep in mind that some dimensions will be off due to printer differences and accuracy
and some changes in 3D model may be needed. Recommended to print and check part by part.

Needed software for raspberry:
Virtual screen and drivers
pygame - Python library
pigpio - for daemon thread to more accurate PWM signal
gpiozero - if installed on other OS
Python 3

Python3 and pygame:
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip install pygame

Virtual screen:
sudo apt-get update
sudo apt-get install libgl1-mesa-dri
export XDG_RUNTIME_DIR=/run/user/$(id -u)

pigpio:
sudo apt-get update
sudo apt-get install pigpio
sudo pip3 install gpiozero

Some other libraries may be needed as whole process wasn't recorded
or unpredictable errors may happen

Elements:
Switch button
Raspberry Pi zero W
Two DC micro motors Pololu 12v with gears. Recommended ratio 1:50
Two transistors MOSFET-N type. Recommended IRFZ44N
Two resistors at least 1000 ohms
Servomechanism 180degrees micro. Recommended Okystar SG-90 micro OR MG-90S - micro
Two Schottky diodes. Recommended SB560
Four batteries 18650 3.7v
USB boost converter step-up
Two AA batteries 1.5v
Springs that will connect and hold batteries
Some shafts (or similar cylinder) Two: 3x20mm AND Four 3:10mm
Two bearings 3x8x3mm [inner hole | outter size | depth]
About 3 screws with nuts M2 10mm
Some wires at least 0.5mm core (for batteries connetcions use much thicker) Recommended: 0.75 or 1mm core
Rubber that will work as a tire for 4 wheels example: scrap of bicycle puncture or something similar

Optional changes:
In case logic level transistor instead of IRFZ44N additional 1.5v batteries may be not needed
Instead of 4 18650 batteries and step up converter - 3 batteries and usb step down converter or other variations

Other needed stuff:
Bluetooth controller (tested with Sony Dualsense controller, other may need some easy changes in code)
Some tape and hot glue
Soldering iron, tin and rosin

Car width: 160mm / 6.29"
Car length: 290mm / 11.41"
Car height: 80mm / 3.14"
Car weight: 500g / 17.63(oz)
