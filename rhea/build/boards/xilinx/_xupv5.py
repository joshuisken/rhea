
from rhea.build import FPGA
from rhea.build.toolflow import ISE 

class XUPV5(FPGA):
    vendor = 'xilinx'
    family = 'virtex5'
    device = 'XC5VLX110T'
    package = 'FF1136'
    speed = '-1'
    _name = 'xupv5'
    
    default_clocks = {
        'clock': dict(frequency=100e6, pins=('AH15',)),
        # 'chan_clk': dict(frequency=1e6, pins=('T7'))
    }
    
    default_resets = {
        'reset': dict(active=0, async=True, pins=('E9',))
    }
    
    default_ports = {
        'led': dict(pins=('AE24', 'AD24', 'AD25', 'G16',
                          'AD26', 'G15',  'L18',  'H18'),
                    iostandard='LVTTL',
                    drive='12',
                    slew='SLOW')
    }

    def get_flow(self, top=None):
        return ISE(brd=self, top=top)
