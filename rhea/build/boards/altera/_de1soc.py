#
# Copyright (c) 2015 Jos Huisken
#

from __future__ import absolute_import

from string import Template

from rhea.build import FPGA
from rhea.build.toolflow import Quartus


class DE1SOC(FPGA):
    vendor = 'altera'
    family = 'Cyclone V'
    device = '5CSEMA5F31C6'
    speed = '6'
    _name = 'de1soc'

    default_clocks = {
        'clock':  dict(frequency=50e6, pins=('AF14',)),
        'clock2': dict(frequency=50e6, pins=('AA16',)),
        'clock3': dict(frequency=50e6, pins=('Y26',)),
        'clock4': dict(frequency=50e6, pins=('K14',))
    }

    default_resets = {
        # 'reset': dict(active=0, async=True, pins=('AH16',))
    }
    
    default_ports = {
        # Need to fix all these...
        'led': dict(pins=('W15', 'AA24', 'V16', 'V15',
                          'AF26', 'AE26', 'Y16', 'AA23',)),
        'key': dict(pins=('AH17')),
        'sw': dict(pins=('L10', 'L9', 'H5', 'H6')),
        
        'gpio': dict(pins=('V12', 'AF7', 'W12', 'AF8', 'Y8', 'AB4',
                           'W8', 'Y4', 'Y5', 'U11', 'T8', 'T12')),
    }

    program_device_cli = (
        Template("quartus_pgm -c \"DE1-SoC [1-1]\" -m jtag -o \"p;$bitfile.sof@2\" "),
             )
    program_nonvolatile_cli = (Template(""),)

    def get_flow(self):
        return Quartus(brd=self)
