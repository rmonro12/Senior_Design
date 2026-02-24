# This code only contains the serial commands in byte form to act as a translator.
#
# Manual stored locally on MSI here:
#    file:///D:\School\UNCC\26%20Spring\1_Senior%20Design%20II\Projector\RS-232_LAN%20Control%20Protocol.pdf
#
# Also stored on team Google Drive in the Elec Schematics folder.

from .serial_comm import ProjectorSerial

POWER_ON_CMD = bytes.fromhex("06 14 00 04 00 34 11 00 00 5D")
POWER_OFF_CMD = bytes.fromhex("06 14 00 04 00 34 11 01 00 5E")

class ProjectorController:
    def __init__(self, serial_iface: ProjectorSerial):
        self.serial = serial_iface

    def power_on(self):
        print("Power ON command triggered")
        self.serial.send_bytes(POWER_ON_CMD)

    def power_off(self):
        self.serial.send_bytes(POWER_OFF_CMD)
    