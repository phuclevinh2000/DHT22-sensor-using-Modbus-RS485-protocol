#lib
import json
import sys
import time
import random
import serial
from iotticket.models import device
from iotticket.models import criteria
from iotticket.models import deviceattribute
from iotticket.models import datanodesvalue
from iotticket.client import Client

port = serial.Serial('COM6', baudrate = 9600, timeout=1);
global received;
port.close();

#main

#data = json.load(open(sys.argv[1]))
data = json.load(open("demo\config.json"))
username = data["username"]
password = data["password"]
deviceId = data["deviceId"]
baseurl = data["baseurl"]

c = Client(baseurl, username, password)

def send_data_to_iot_ticket(value,value2):
    print("WRITE DEVICE DATANODES FUNTION.")
    listofvalues=[]
    nv = datanodesvalue()
    nv.set_name("Humidity") #needed for writing datanode
    nv.set_path("hum")
    nv.set_dataType("double")
    nv.set_unit("%")
    nv.set_value(value) #needed for writing datanode
    nv1 = datanodesvalue()
    nv1.set_name("Temperature") #needed for writing datanode
    nv1.set_path("temp")
    nv1.set_dataType("double")
    nv1.set_unit("C")
    nv1.set_value(value2) #needed for writing datanode
    listofvalues.append(nv)
    listofvalues.append(nv1)
    print(c.writedata(deviceId, *listofvalues)) # another way to make this would be c.writedata(deviceId, nv, nv1)
    print("END WRITE DEVICE DATANODES FUNCTION")
    print("-------------------------------------------------------\n")

def modbus_request(hexadecimal_string):
    
        #01 04 00 01 00 01 60 0A
        #https://rapidscada.net/modbus/ModbusParser.aspx
    print("request",hexadecimal_string);
    port.open();
    port.write(hexadecimal_string);
    received=port.read(8);
    print("respond",received);  #error in respond frame, just 6 instead of 7 byte responded
    value=((received[3]<<8)|received[4])&0x0FFF; #adc value to real value
    time.sleep(1);
    port.close();
    return value;

while True:
    hexadecimal_string1 = [0x08,0x04,0x00,0x01,0x00,0x01,0x60,0x93];
    hexadecimal_string2 = [0x08,0x04,0x00,0x02,0x00,0x01,0x90,0x93];
    #write datanode demo
    value=modbus_request(hexadecimal_string2)/10.0; #humidity value
    value2=modbus_request(hexadecimal_string1)/10.0; #read temperature and divided by 10 (*-1 for demo)
    print(value,"Humitidy")
    print(value2,"Celsius")
    send_data_to_iot_ticket(value,value2); 
    time.sleep(10);
