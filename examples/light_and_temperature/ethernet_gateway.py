# green LED is on GPIO PA6
greenLed = ["greenLed", "PA6", "digital", "grLedF", 1]
greenValues = ["discrete", 2, "off", "on"]

# red LED is on GPIO PA7
redLed = ["redLed", "PA7", "digital", "rdLedF", 1]
redValues = ["discrete", 2, "off", "on"]

# button is on GPIO PA3
buttonPoint = ["button", "PA3", "digital", "buttonF", 1]
buttonValues = ["discrete", 2, "up", "down"]

# Конфигурация шлюза
celPy.ApplicationName = "MeshWorks"
celPy.DeviceName = "Gateway"
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [buttonPoint]
celPy.DataCollectionValues = [buttonValues]
celPy.ControlPoints = [greenLed, redLed]
celPy.ControlValues = [greenValues, redValues]

# Обработка сообщений от других сетевых устройств
def cpCallbackDataPointMessageReceived(deviceName, datapointName, discreteValueString, rangeValue):
    if (deviceName == "Sensor 1"):
        if (datapointName == "button"):
            udpPayload = deviceName
            udpPayload = (udpPayload + ": button=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("192.168.22.225", 5555, udpPayload)
        if (datapointName == "tempSensor"):
            udpPayload = deviceName
            udpPayload = (udpPayload + ": temp=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("192.168.22.225", 5555, udpPayload)
    if (deviceName == "Sensor 2"):
        if (datapointName == "button"):
            udpPayload = deviceName
            udpPayload = (udpPayload + ": button=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("192.168.22.225", 5555, udpPayload)
        if (datapointName == "tempSensor"):
            udpPayload = deviceName
            udpPayload = (udpPayload + ": temp=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("192.168.22.225", 5555, udpPayload)

def main():
    pass
