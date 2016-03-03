import os
import sys
sys.path.insert(0, os.path.join(os.path.expanduser('~huisken'),'s/lib'))

from qsf import qsf 
import pickle

def de1():
    de1 = os.path.join(os.path.expanduser('~huisken'),'s/boards/de1/ghrd/soc_system.qsf')
    q = qsf(de1)

    # print q.loc_ass
    defports = {}

    p = [q.loc_ass[k] for k in ['LEDR[%d]' % (i) for i in range(10)]]
    defports['led'] = dict(pins = tuple(p))

    p = [q.loc_ass[k] for k in ['SW[%d]' % (i) for i in range(10)]]
    defports['sw'] = dict(pins = tuple(p))

    p = [q.loc_ass[k] for k in ['KEY[%d]' % (i) for i in range(4)]]
    defports['key'] = dict(pins = tuple(p))

    p = [q.loc_ass[k] for k in ['GPIO_0[%d]' % (i) for i in range(36)]]
    defports['gpio0'] = dict(pins = tuple(p))

    p = [q.loc_ass[k] for k in ['GPIO_1[%d]' % (i) for i in range(36)]]
    defports['gpio1'] = dict(pins = tuple(p))

    for k in ['HEX%d' % (i) for i in range(6)]:
        p = [q.loc_ass[j] for j in ['%s[%d]' % (k, i) for i in range(7)]]
        defports[k.lower()] = dict(pins = tuple(p))

    print defports

    # p = [q.loc_ass[k] for k in ['HPS_GPIO[%d]' % (i) for i in range(2)]]

    # resetports = {}
    # p = [q.loc_ass[k] for k in ['HPS_NPOR', 'HPS_NRST']]
    # resetports['reset'] = dict(pins = tuple(p))
    # print resetports


    with open('de1.pckl', 'w') as f:
        pickle.dump(defports, f)


def c5():
    c5 = os.path.join(os.path.expanduser('~huisken'),'s/boards/veek/cv_soc_devkit_ghrd/soc_system.qsf')
    q = qsf(c5)

    # print q.loc_ass
    defports = {}

    p = [q.loc_ass[k] for k in ['fpga_led_pio[%d]' % (i) for i in range(4)]]
    defports['led'] = dict(pins = tuple(p))

    p = [q.loc_ass[k] for k in ['fpga_dipsw_pio[%d]' % (i) for i in range(4)]]
    defports['sw'] = dict(pins = tuple(p))

    p = [q.loc_ass[k] for k in ['fpga_button_pio[%d]' % (i) for i in range(2)]]
    defports['key'] = dict(pins = tuple(p))

    print defports

    with open('c5.pckl', 'w') as f:
        pickle.dump(defports, f)



if __name__ == '__main__':
    try:
        q = qsf(sys.argv[1])
    except:
        de1()
        c5()
