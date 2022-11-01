from time import sleep

from gpiozero import LED

from opener.internal.env import Envs

SWITCH = LED(Envs().gate_pin)


def trigger_gate() -> None:
    """Trigger the gate pin on pi"""
    SWITCH.on()
    sleep(0.1)
    SWITCH.off()
