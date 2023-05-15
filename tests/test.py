import prologixGPIBEthernetCustom

ctrl1 = prologixGPIBEthernetCustom.PrologixGPIBEthernetCustom('BI-GPIB-02', timeout=10)
ctrl1.connect()
ctrl1.set_gpib_address(2)


ctrl2 = prologixGPIBEthernetCustom.PrologixGPIBEthernetCustom('BI-GPIB-03', timeout=10)
ctrl2.connect()
ctrl2.set_gpib_address(4)

import time
k = 0
while True: 
    print(k, ctrl1.serial_poll())
    k += 1
    time.sleep(1)

    