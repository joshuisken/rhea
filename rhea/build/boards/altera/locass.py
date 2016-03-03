import os
import sys
sys.path.insert(0, os.path.join(os.path.expanduser('~huisken'),'s/lib'))

from qsf import qsf 
import pickle

if __name__ == '__main__':
    de1 = os.path.join(os.path.expanduser('~huisken'),'s/boards/de1/ghrd/soc_system.qsf')
    try:
        q = qsf(sys.argv[1])
    except:
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

    with open('de1.pckl', 'w') as f:
        pickle.dump(defports, f)
