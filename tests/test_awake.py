import time 
import prologixGPIBEthernetCustom
import attenuator_511A

ctrl1 = prologixGPIBEthernetCustom.PrologixGPIBEthernetCustom('BI-GPIB-02', timeout=10)
ctrl1.connect()
ctrl2 = prologixGPIBEthernetCustom.PrologixGPIBEthernetCustom('BI-GPIB-03', timeout=10)
ctrl2.connect()

att_L = attenuator_511A.Attenuator_511A(2, ctrl1)
att_R = attenuator_511A.Attenuator_511A(4, ctrl2)

# stress test
import numpy as np
k = 0
fail_L_cnt = 0
fail_R_cnt = 0

while True:
    print(k)
    try:
        att_L.set_attenuator( int(60*np.random.uniform()) ) 
    except:
        print('L failed')
        fail_L_cnt += 1

    try:
        att_R.set_attenuator( int(60*np.random.uniform()) ) 
    except:
        print('R failed')
        fail_R_cnt += 1

    k += 1

    if k == 4300:
        break

att_L.controller.close()
att_R.controller.close()

print('Test finished:')
print('L failed ', fail_L_cnt, ' times.')
print('R failed ', fail_R_cnt, ' times.')
print('----------')