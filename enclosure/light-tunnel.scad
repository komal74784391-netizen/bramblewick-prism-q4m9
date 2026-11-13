// Prism optical tunnel
$fn = 64;

tunnel_length = 38;
tunnel_diameter = 12;

module tunnel() {
    difference() {
        cylinder(h = tunnel_length, d = tunnel_diameter + 4, center = true);
        cylinder(h = tunnel_length + 1, d = tunnel_diameter, center = true);
    }
}

module cassette_slot() {
    translate([0, 0, tunnel_length / 2 - 3])
        cube([26, 3.2, 6], center = true);
}

tunnel();
cassette_slot();
