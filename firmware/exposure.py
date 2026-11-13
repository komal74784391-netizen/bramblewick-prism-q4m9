"""Named exposure profiles for the Prism reader."""

PROFILES = {
    "fast": 0.2,
    "standard": 0.8,
    "slow": 2.0,
}


def seconds(name):
    if name not in PROFILES:
        raise ValueError("unknown exposure profile: {}".format(name))
    return PROFILES[name]


def list_profiles():
    return sorted(PROFILES.items())
