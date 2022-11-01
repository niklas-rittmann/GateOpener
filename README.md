# :electric_plug: GateOpener

## :closed_lock_with_key: Summary
GateOpener is exactly what the name implies: Its a piece of software that allows you to open a gate (or whatever electronic device) normally operated with a switch. You can controll the device using your computer or phone simply by sending a HTTP-request to the webserver. To close the gap between your computer and the device your trying to control you only need a raspberry pi or similar device.
Because its docker based the setup is as easy as it could be, just start the image on your raspberry pi and youre ready to go.

## :question: Why though?
Whats the device youre always missing? Remotes. Whats the one device you always have on youre hand? Youre phone. Thats why.

## :electric_plug: How to get started
### :shopping_cart: As said before you need the following components:
- Raspberry Pi or similar with a running instance of docker
- An electronnaly controllable switch (Relais, Optocoupler, Transistor whatever)
- A device you want to control

### :satellite: Wiring
Connect youre controllable switch to the raspberry pi and youre device. By default the GPIO Pin 2 of the pi is used, but you can change it using the `GATE_PIN` environment variable.

### :checkered_flag: Starting the app
By default the app runs on port 8000. You can change the port using `BACKEND_PORT`.
```bash
docker run --device /dev/gpiomem -p 80:80 -d --env GATE_PIN=2 --env BACKEND_PORT=80 gate_opener:0.0.1
```
## :construction: Roadmap
- [ ] Enable Https
- [ ] Add status endpoint
