"""Debounce a Pin."""
from machine import Pin, Timer


class Debounce:
    """Debounce Pin."""

    debug = False

    def __init__(self, pin, func, desired=None, **kwargs) -> None:
        self.pin = pin
        self.timer = None
        self.desired = self.pin.value() if desired is None else desired
        self.counter = 0
        self.func = func
        self.kwargs = kwargs
        # Set up interrupt handler
        pin.irq(self.start_debounce, Pin.IRQ_FALLING | Pin.IRQ_RISING)

    def new_timer(self):
        """Start a new Timer and call back."""
        timer = Timer(0)
        timer.init(
            mode=Timer.ONE_SHOT,
            period=50,
            callback=self.check_debounce,
        )
        return str(timer)

    def start_debounce(self, pin):
        """Start Timer for debouncing."""
        pin = str(pin)
        val = "HIGH" if self.pin.value() == 1 else "LOW"
        if self.debug:
            print(f"Pin: {pin} Value: {val}")

        if self.timer is None:
            self.timer = self.new_timer()
            self.counter += 1
        else:
            if self.debug:
                print("Existing Timer already started")

    def check_debounce(self, timer):
        """Check passes and maybe trigger callback."""
        if self.debug:
            print(f"Counter: {self.counter}")

        timer = str(timer)
        if self.debug:
            print(f"Timer: {timer}")

        pin = str(self.pin)
        val = self.pin.value()
        if self.debug:
            print(f"Pin: {pin}: {val}")

        if self.desired == val:  # welcome back to desired state
            runs = self.counter  # save count to runs
            self.counter = 0  # reset counter before we might trigger
            if runs > 1:  # more then one run through
                self.func(self.pin, **self.kwargs)  # trigger
            else:
                print(f"{pin}: debounced, baby!")

        self.timer = None
