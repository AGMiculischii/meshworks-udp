# Handle UDP datagrams from CEL's Ethernet gateway

This is the test UDP server which helps to understand the flow how all incoming
datagrams may be processed on the server side in a user application.

For example, you have a gateway and two sensor nodes which send periodically some
status information to the gateway (like push-buttons status, temperature data etc.)
If you want somehow represent this data it will be helpful to parse incoming data.

Here is the example of the case:

**Node's messages to the gateway**
```python
button = 1 or button = 0
# temperature in the degrees of Celcius
temperature = ...
```

The gateway collects that data and then send an UDP message to a user server:

**Gateway's data format**

```python
# udpPayload is a string
# on each step we append necessary value
# deviceName = name of the device which sent data to the gateway
udpPayload = deviceName
# instead of button might be another string variable which represents type
# of an incoming parameter
udpPayload = (udpPayload + ": button=")
# append value which sensor node sended to the gateway
udpPayload = (udpPayload + rangeValue)
# send that payload to the server
# according to MeshWorks syntax - address is string, port is int, udpPayload is
# string
udp.send("<address>", port, udpPayload)
```

After that on the server side user application can process as it necessary:
  * Send to a database
  * Output to GUI
  * Output to console
  * Process and alert
  * Something else

This repository example simply pass whole UDP data to the console output
