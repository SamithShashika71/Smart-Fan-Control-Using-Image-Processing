# 🌬️ Smart Fan Controlled by Image Processing

A **gesture-controlled smart fan system** that combines **computer vision** with **embedded hardware** to create an intelligent, touch-free fan control system.

Using **OpenCV**, **MediaPipe**, and **Arduino Uno**, the system recognizes real-time hand gestures through a camera and adjusts the fan’s behavior accordingly.

---

## 🚀 Features
- 🖐️ **Gesture-Based Control** – Turn the fan ON/OFF using simple hand gestures.  
- 🔄 **Speed Adjustment** – Increase or decrease the fan speed dynamically.  
- ⚙️ **Level Control** – Set the fan to specific speed levels via gesture.  
- ⚡ **Real-Time Processing** – Fast and accurate gesture detection using MediaPipe.  
- 💻 **Python-Arduino Communication** – Control hardware through PyFirmata and PWM signals.  

---

## 🔧 Tech Stack
| Component | Technology Used |
|------------|----------------|
| Programming Language | Python |
| Computer Vision | OpenCV, MediaPipe |
| Microcontroller | Arduino Uno |
| Communication | PyFirmata |
| Hardware | PWM Fan, MOSFET |
| Signal Control | PWM (Pulse Width Modulation) |

---

## 🧠 Concepts & Skills Learned
- Real-time **gesture recognition** using computer vision.  
- **Serial communication** between Arduino and Python.  
- Hardware control through **PWM signals**.  
- Integration of **AI with embedded systems**.  
- **IoT prototyping** with image processing.  

---

## 🏗️ System Overview
1. **Camera Input** – Captures real-time hand gestures.  
2. **MediaPipe Processing** – Detects and tracks hand landmarks.  
3. **Gesture Classification** – Recognizes gestures for ON/OFF and speed control.  
4. **Arduino Communication** – Sends control signals to Arduino via PyFirmata.  
5. **Fan Response** – Adjusts speed or toggles power using PWM and MOSFET driver.  

---

## ⚙️ Setup Instructions
1. Install dependencies:
   ```bash
   pip install opencv-python mediapipe pyfirmata
Connect Arduino Uno via USB.

Upload the StandardFirmata sketch to Arduino using the Arduino IDE.

Run the Python script:
python smart_fan_control.py

Show your hand gestures to the camera to control the fan!

---
🧩 Hardware Requirements
Arduino Uno board

12V PWM fan

N-channel MOSFET

External power supply

USB cable

Breadboard and jumper wires

---
🌐 Future Enhancements
Add temperature sensors for auto speed adjustment.

Enable Wi-Fi or Bluetooth control.

Implement voice commands for hybrid control.

Design a mobile dashboard for monitoring and settings.

---
❤️ Acknowledgement
This project was developed as part of my university coursework to explore AI-driven hardware control.
It demonstrates how computer vision and embedded systems can merge to create smart home automation solutions. 🏡✨
