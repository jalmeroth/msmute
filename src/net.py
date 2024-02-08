import network
from machine import unique_id
from ubinascii import hexlify


class NetworkManager:
    """NetworkManager represenation."""

    def disable_ap_mode(self):
        """Disable default AP-mode."""
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(False)
        print("AP-mode disabled.")
        del ap_if

    def do_connect(self, ssid, password, hostname=None):
        """Connect to WiFi."""
        self.disable_ap_mode()
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if hostname is None:
            hostname = self.generate_hostname()
        wlan.config(dhcp_hostname=hostname)
        if not wlan.isconnected():
            print("connecting to network...")
            wlan.connect(ssid, password)
            while not wlan.isconnected():
                pass
        print("network config:", wlan.ifconfig())

    def generate_hostname(self):
        """Generate a hostname from unique_id."""
        prefix = "ESP"
        uid = hexlify(unique_id()).decode()[6:12]
        return f"{prefix}_{uid}".upper()
