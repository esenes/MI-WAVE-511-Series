import prologixGPIBEthernetCustom
import time

class Attenuator_511A:

    def __init__(self, GPIB_address, controller):
        self.GPIB_address = GPIB_address
        self.controller = controller

        self.controller.set_gpib_address(self.GPIB_address)

    def ping(self):
        return self.controller.serial_poll()


    def set_attenuator(self, value, wait_after_move=5):
        if len(self.ping()) > 0:
            self.controller.set_attenuation(value, self.GPIB_address)
            time.sleep(wait_after_move)
        else:
            print('Something went wrong')