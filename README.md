# GateOpener
## 🔐 Summary
GateOpener is exactly what the name implies: Its a piece of software that allows you to open a gate (or whatever electronic device) normally operated with a switch. You can control the device using your computer or phone simply by sending a HTTP-request to the webserver. To close the gap between your computer and the device you are trying to control you only need a raspberry pi or similar device. Because its docker based the setup is as easy as it could be, just start the image on your raspberry pi and you are ready to go.

## ❓ Why though?
Whats the device you are always missing? Your remote. Whats the one device you always have on your hand? Youre phone. Thats why.

## 🔌 How to get started
### 🛒 As said before you need the following components:
- Raspberry Pi or similar with a running instance of docker
- An electronic controllable switch (Relais, Optocoupler, Transistor whatever)
- A device you want to control
### 📡 Wiring
Connect your controllable switch to the raspberry pi and your device. By default the GPIO Pin 2 of the pi is used, but you can change it using the `GATE_PIN` environment variable.

### 🏁 Starting the app
By default the app runs on port 8000. You can change the port using `BACKEND_PORT`.
You need to perform some configuration, for that its best to create an env file like the following:
```bash
USERNAME= # The username you want to login with
PASSWORD= # The password for the specified user
GATE_PIN= # The gpio pin of your raspberry pi
BACKEND_PORT= # Defaults to 8000
SECRET_KEY= # Optional: Provide an own secret key, otherwise one is generated using openssl rand -hex 32
```
```bash
docker run --device /dev/gpiomem -p 80:80 -d --env-file .env niklasrittmann/gate_opener:0.0.1
```
## 🚧 Roadmap
- [x] Authentification
- [ ] Enable Https
- [ ] Add status endpoint

## Disclaimer
Use at your own risk! Software is always vulnerable!
