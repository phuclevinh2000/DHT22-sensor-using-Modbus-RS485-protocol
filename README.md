# DHT22-sensor-using-Modbus-RS485-protocol
The project is made for studying and researching of Embedded system design purpose. It is also a reference of how to use DHT22 – temperature and humidity sensor in an em-bedded system, then send the data to the master device. This project will focus on the DHT22 sensor and how to receive and send the signal to the master device. When the master sends out the request signal, we will respond by sending the value of humidity or temperature corresponding.


In this project, we design the system by testing it on the breadboard, using STM32L152RE to process the temperature and humidity data, then send the result to the master device. In this course, we used a python program that queries the data from different slave devices (one is our) and saves the data in the Wapice IoT ticket, and we have successfully sent our results to the IoT ticket.

This is the main important file, and for the template, we will the STM32 template 
