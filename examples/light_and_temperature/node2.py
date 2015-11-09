# Светодиод на выводе PA6 
greenLed = ["greenLed", "PA6", "digital", "grLedF", 1]
greenValues = ["discrete", 2, "off", "on"]
# Светодиод на выводе PA7
redLed = ["redLed", "PA7", "digital", "rdLedF", 1]
redValues = ["discrete", 2, "off", "on"]

# Data Point для кнопки
button = ["button", "PB6", "digital", "buttonF", 1]
bValues = ["discrete", 2, "up", "down"]

prevButtonValue = 0
buttonTickCount = 0

def buttonF():
    value = readDigital()
    # Периодическая отправка данных
    # о состоянии выключателя
    if (buttonTickCount > 30):
        buttonTickCount = 0
        sendDataReport(value, "button state")
    # если значение поменялось
    if (value != prevButtonValue):
        sendDataReport(value, "button state")
        # Устанавливаем состояние светодиода
        # в соответствии с состоянием выключателя
        celPy.AdjustLocalControlPoint("greenLed", value)
    prevButtonValue = value
    buttonTickCount = (buttonTickCount + 1)

# Data Point для датчика температуры
tempSensor = ["tempSensor", "PA1", "i2c", "tempMeasFunc", 20]
tempSensorValues = ["range", -40, 120]

# Чтение температуры с Si7013
def tempMeasFunc():
    value = readI2c(0x41, 0xE3, bigEndian)
    # Преобразование в градусы Цельсия
    value = (value * 175)
    value = (value / 65535)
    value = (value - 47)
    sendDataReport(value, "degrees C")

celPy.addTickFunction(heartbeatLed, 20)

ledState = 0

def heartbeatLed():
    if (ledState == 0):
        celPy.AdjustLocalControlPoint("redLed", 1)
        ledState = 1
        return
    if (ledState == 1):
        celPy.AdjustLocalControlPoint("redLed", 0)
        ledState = 0

####################################################
# Сетевые настройки
celPy.ApplicationName = "MeshWorks"
celPy.DeviceName = "Sensor 2"
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [button, tempSensor]
celPy.DataCollectionValues = [bValues, tempSensorValues]
celPy.ControlPoints = [greenLed, redLed]
celPy.ControlValues = [greenValues, redValues]

def main():
    pass
