"""Prism plate reader serial protocol."""

import time

import exposure
import light_sensor
import plate


def scan_well(cassette, profile):
    light_sensor.select(cassette)
    light_sensor.reset()
    time.sleep(exposure.seconds(profile))
    return light_sensor.read_raw()


def scan_plate(cassette, template, profile="standard"):
    readings = []
    for well in plate.iter_wells(template):
        plate.position(well)
        readings.append({"well": well.name, "value": scan_well(cassette, profile)})
    return readings


def handle_command(line):
    parts = line.strip().split()
    if not parts:
        return "ERR empty"
    if parts[0] == "scan":
        cassette, profile = parts[1], parts[2]
        return scan_plate(cassette, plate.current(), profile)
    if parts[0] == "profile":
        return exposure.list_profiles()
    return "ERR unknown"


if __name__ == "__main__":
    print(handle_command("profile list"))
