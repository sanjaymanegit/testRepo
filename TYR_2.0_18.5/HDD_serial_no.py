import wmi
c = wmi.WMI()
hddSerialNumber = c.Win32_PhysicalMedia()[0].wmi_property('SerialNumber').value.strip()
print(hddSerialNumber)