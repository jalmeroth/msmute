$fn=100;
// wall
$ws=2;
// box
$by=50-2*$ws;
$bx=119-2*$ws;
$bz=10-$ws;


translate([$ws,$ws,0])
difference() {
    union() {
        cube([$bx,$by,$bz]);
        translate([-$ws,$by/2,$bz/2])
        rotate([0,90,0])
        cylinder(h=119,d=3);
    }
    translate([$ws,$ws,$ws])
    cube([$bx-2*$ws,$by-2*$ws,$bz-$ws+3]);
}
