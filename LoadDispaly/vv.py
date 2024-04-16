try:
    check_driver = self.device.is_kernel_driver_active(0)
except NotImplementedError:
    pass
if check_driver is None or check_driver:
    try:
        device.detach_kernel_driver(0)
    except usb.core.USBError as e:
        if check_driver is not None:
            print("Could not detatch kernel driver: {0}".format(str(e)))