$fn=100;
// wall
$ws=2;
// box
$by=50;
$bx=119;
$bz=50;
// knops
$kd=24;
$kr=$kd/2;
// cable
$cx=6;
$cy=10;

difference() {
    cube([$bx,$by,$bz]);
    translate([$ws,$ws,$ws])
    cube([$bx-2*$ws,$by-2*$ws,$bz-$ws]);
    translate([2*$ws,0,0])
    union() {
        for(i=[0:3]) {
            $x=$kr+(i*($kd+5));
            echo($x);
            translate([$x,$by/2,0])
            cylinder(h=$ws, d=$kd);
        }
    }
    // Power cable
    translate([$ws,($by-$cy)/2,$bz-$cx-10])
    rotate([0,-90,0])
    cube([$cx,$cy,$ws]);
    // Closing
    translate([0,$by/2,$bz])
    rotate([0,90,0])
    cylinder(h=$bx,d=3);
}
