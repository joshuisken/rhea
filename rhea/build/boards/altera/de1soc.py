#
# Copyright (c) 2015 Jos Huisken
#

from __future__ import absolute_import

from string import Template

from rhea.build import FPGA
from rhea.build.toolflow import Quartus

import pickle

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

    # It looks like there's no dedicated reset pin for FPGA part
    default_resets = {
        'reset': dict(active=0, async=True)  # Should come from HPS side.
    }
    
    # Could use this:
    # with open('de1.pckl', 'r') as f:
    #     default_ports = pickle.load(f)

    default_ports = {
        'gpio0': {'pins': ('AC18', 'Y17', 'AD17', 'Y18', 'AK16', 'AK18',
                           'AK19', 'AJ19', 'AJ17', 'AJ16', 'AH18', 'AH17',
                           'AG16', 'AE16', 'AF16', 'AG17', 'AA18', 'AA19',
                           'AE17', 'AC20', 'AH19', 'AJ20', 'AH20', 'AK21',
                           'AD19', 'AD20', 'AE18', 'AE19', 'AF20', 'AF21',
                           'AF19', 'AG21', 'AF18', 'AG20', 'AG18', 'AJ21')},
        'gpio1': {'pins': ('AB17', 'AA21', 'AB21', 'AC23', 'AD24', 'AE23',
                           'AE24', 'AF25', 'AF26', 'AG25', 'AG26', 'AH24',
                           'AH27', 'AJ27', 'AK29', 'AK28', 'AK27', 'AJ26',
                           'AK26', 'AH25', 'AJ25', 'AJ24', 'AK24', 'AG23',
                           'AK23', 'AH23', 'AK22', 'AJ22', 'AH22', 'AG22',
                           'AF24', 'AF23', 'AE22', 'AD21', 'AA20', 'AC22')},
        'led': {'pins': ('V16', 'W16', 'V17', 'V18', 'W17', 'W19', 'Y19', 'W20', 'W21', 'Y21')},
        'sw': {'pins': ('AB12', 'AC12', 'AF9', 'AF10', 'AD11', 'AD12', 'AE11', 'AC9', 'AD10', 'AE12')},
        'key': {'pins': ('AA14', 'AA15', 'W15', 'Y16')},
        'hex0': {'pins': ('AE26', 'AE27', 'AE28', 'AG27', 'AF28', 'AG28', 'AH28')},
        'hex1': {'pins': ('AJ29', 'AH29', 'AH30', 'AG30', 'AF29', 'AF30', 'AD27')},
        'hex2': {'pins': ('AB23', 'AE29', 'AD29', 'AC28', 'AD30', 'AC29', 'AC30')},
        'hex3': {'pins': ('AD26', 'AC27', 'AD25', 'AC25', 'AB28', 'AB25', 'AB22')},
        'hex4': {'pins': ('AA24', 'Y23', 'Y24', 'W22', 'W24', 'V23', 'W25')}}
        'hex5': {'pins': ('V25', 'AA28', 'Y27', 'AB27', 'AB26', 'AA26', 'AA25')},

    program_device_cli = (
        Template("quartus_pgm -c \"DE1-SoC [1-1]\" -m jtag -o \"p;$bitfile.sof@2\" "),
             )
    program_nonvolatile_cli = (Template(""),)

    def get_flow(self):
        return Quartus(brd=self)
