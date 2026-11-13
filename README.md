# Bramblewick Prism

Open-source design package for the Prism absorbance plate reader.

## Implementation

Prism uses three swappable LED cassettes (405 nm, 450 nm and 630 nm) and a
TSL2591 light sensor. The reader head is a printed optical tunnel with machined
cassette detents; the controller is an RP2040 on a two-layer board.

- `hardware/` - KiCad schematic and board layout.
- `firmware/` - serial protocol, scan sequencing and exposure profiles.
- `enclosure/` - optical tunnel and cassette models.
- `docs/` - optics alignment notes.

## Build

Flash `firmware/reader.py` and `firmware/exposure.py`. The serial protocol
accepts named exposure profiles (`fast`, `standard`) and a plate template.

The LED cassettes are not interchangeable between revisions; revision B uses
the taller detent.
