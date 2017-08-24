# NEW LAB, IoT

Welcome! 

A development environment is setup for you in Linux.

This toolchain setup for MicroPython for ESP32, with 4MB psRAM support and esp-idf building system is courtesy of the open source community and you can read more about it here:

[https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo)


Let's get started.


#### All build commands will be run from this location:

	cd ~/MicroPython_ESP32_psRAM_LoBo/MicroPython_BUILD

#### Flashing the file system to the board means running this command:

	./BUILD.sh flashfs

#### A view of the running application is available with this command:
	./BUILD.sh monitor


#### LEDs

[Let's light things up](https://github.com/areaofeffect/newlab-iot-workshop/tree/master/LED)

#### PIEZO

[Sensing the world through vibration](https://github.com/areaofeffect/newlab-iot-workshop/tree/master/PIEZO)

#### PPG

[Getting biometric](https://github.com/areaofeffect/newlab-iot-workshop/tree/master/PPG)


![Hero](https://images.contentful.com/kifoc1e7z7rr/3IEjxSIKesIS06co28a0SK/d629d435be55c6a3af59ecd5d85e3afb/Hero-Shot.jpg)

<br/>
<br/>

We are here to teach you how to talk to machines and are proud to present you The New Lab IoT board. We developed a new way to prototype ideas, sense the world and connect with our fellow humans and machines.

Our platform is as capable as Raspberry Pi, AdaFruit and Intel IoT boards. It's faster than some other off the shelf boards out now. It ships out-of-the-box with BLE, WiFi, environmental and biometric sensing capabilities. We can't wait to see what new ideas you come up with while hacking with it.


We hope you love building with it as much as we loved making it.

*- Area of Effect*

<br />

#### Get by with a little from our friends

AoE thanks all those that helped us bring this idea into reality. 10xBeta, New Lab, dagtronix, @johngineer


##### Further reading / viewing

[ESP-IDF](https://esp-idf.readthedocs.io/en/v2.1/index.html)

[MicroPython](https://micropython.org/)

[MicroPython Github](https://github.com/micropython)

[Pulse Oximeter](https://morf.lv/implementing-pulse-oximeter-using-max30100)

[GOTO 2016 • MicroPython & the Internet of Things • Damien George](https://www.youtube.com/watch?v=EvGhPmPPzko)

[The Humane Representation of Thought • Bret Victor](https://vimeo.com/115154289)


#### Standing on the shoulders of giants

We ported many things originally written for Arduino to Micropython. Here's the license info. Much respect.

MAX301015

```
/***************************************************
  This is a library written for the Maxim MAX30105 Optical Smoke Detector
  It should also work with the MAX30102. However, the MAX30102 does not have a Green LED.
  These sensors use I2C to communicate, as well as a single (optional)
  interrupt line that is not currently supported in this driver.
  Written by Peter Jansen and Nathan Seidle (SparkFun)
  BSD license, all text above must be included in any redistribution.
 *****************************************************/
```
 
HeartRate

```
/*
 Optical Heart Rate Detection (PBA Algorithm)
 By: Nathan Seidle
 SparkFun Electronics
 Date: October 2nd, 2016
 
 Given a series of IR samples from the MAX30105 we discern when a heart beat is occurring
 Let's have a brief chat about what this code does. We're going to try to detect
 heart-rate optically. This is tricky and prone to give false readings. We really don't
 want to get anyone hurt so use this code only as an example of how to process optical
 data. Build fun stuff with our MAX30105 breakout board but don't use it for actual
 medical diagnosis.
 Excellent background on optical heart rate detection:
 http://www.ti.com/lit/an/slaa655/slaa655.pdf
 Good reading:
 http://www.techforfuture.nl/fjc_documents/mitrabaratchi-measuringheartratewithopticalsensor.pdf
 https://fruct.org/publications/fruct13/files/Lau.pdf
 This is an implementation of Maxim's PBA (Penpheral Beat Amplitude) algorithm. It's been 
 converted to work within the Arduino framework.
*/

/* Copyright (C) 2016 Maxim Integrated Products, Inc., All Rights Reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included
* in all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
* OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
* IN NO EVENT SHALL MAXIM INTEGRATED BE LIABLE FOR ANY CLAIM, DAMAGES
* OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
* ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
* OTHER DEALINGS IN THE SOFTWARE.
*
* Except as contained in this notice, the name of Maxim Integrated
* Products, Inc. shall not be used except as stated in the Maxim Integrated
* Products, Inc. Branding Policy.
*
* The mere transfer of this software does not imply any licenses
* of trade secrets, proprietary technology, copyrights, patents,
* trademarks, maskwork rights, or any other form of intellectual
* property whatsoever. Maxim Integrated Products, Inc. retains all
* ownership rights.
* 
*/
```

Piezo Secret Knock

```
   Originally from Steve Hoefer http://grathio.com Version 0.1.10.20.10
   Updates by Lee Sonko

   Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0
   http://creativecommons.org/licenses/by-nc-sa/3.0/us/
   
 ```