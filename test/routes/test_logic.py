from opener.internal import logic


class Mockswitch:
    state = None

    def on(self) -> None:
        self.state = True

    def off(self) -> None:
        self.state = False


def test_trigger_gate_status(monkeypatch) -> None:
    """Test that the status change works"""
    switch = Mockswitch()
    monkeypatch.setattr(logic, "SWITCH", switch)

    logic.trigger_gate()
    assert switch.state == False
