#
# Copyright (c) 2015 Jos Huisken
#

from __future__ import absolute_import

from string import Template

from rhea.build import FPGA
from rhea.build.toolflow import Quartus

import pickle

class C5SOC(FPGA):
    vendor = 'altera'
    family = 'Cyclone V'
    device = '5CSXFC6D6F31C6'
    speed = '6'
    _name = 'c5soc'

    default_clocks = {
        'clock':  dict(frequency=50e6, pins=('AC18',)),
    }

    default_resets = {
        'reset': dict(active=0, async=True, pins=('AD27',))
    }
    
    # Could use this:
    # with open('c5.pckl', 'r') as f:
    #     default_ports = pickle.load(f)

    default_ports = {
        'sw': {'pins': ('AG10', 'AH9', 'AF11', 'AG11')},
        'led': {'pins': ('AK2', 'Y16', 'W15', 'AB17')},
        'key': {'pins': ('AA13', 'AB13')}
    }

    program_device_cli = (
        Template("quartus_pgm -c \"C5-SoC [1-1]\" -m jtag -o \"p;$bitfile.sof@2\" "),
             )
    program_nonvolatile_cli = (Template(""),)

    def get_flow(self):
        return Quartus(brd=self)
