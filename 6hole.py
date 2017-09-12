from solid import * 
from solid.utils import *
from math import *

#variable definitions for flute calculations
holeCount=6;  # Number of flute finger holes
Xend = 0; # initialize effective location of end of flute
Xf = [0,0,0,0,0,0,0,0,0,0];  # initialize location of finger holes
Xemb = 0; # initialize location of embouchure
Ff = [0]
C0 = 16.35 #C0 frequency in hertz
Vsound = 345000; #velocity of sound mm/second. for inch/second use 13584

#the different musical modes
ionian = [2,4,5,7,9,11,12]#[2,2,1,2,2,2,1]
dorian = [2,3,5,7,9,10,12]#[2,1,2,2,2,1,2]
phygrian = [1,3,5,7,8,10,12]#[1,2,2,2,1,2,2]
lydian = [2,4,6,7,9,11,12]#[2,2,2,1,2,2,1]
mixolydian = [2,4,5,7,9,10,12]#[2,2,1,2,2,1,2]
aeolian = [2,3,5,7,8,10,12]#[2,1,2,2,1,2,2]
locrian = [1,3,5,6,8,10,12]#[1,2,2,1,2,2,2]

###################################
#CHANGE THE VARIABLES YOU WANT HERE
key = 'E' #input A, A#, B, C, C#, D, D#, E, F, F#, G, G# ... C4 to B4
mode = ionian #ionian, dorian, phrygian, lydian, mixolydian, aeolian, locrian
Bore = 14; #inside diameter of tube  #17.5mm outer diameter 
wall = 1.7; # wall thickness of tube
Demb = 10.0; # embouchure hole diameter
#Df = [0,10.0,9.5,7.0,9.0,8.5,8.0,0,0,0] # finger hole diameters
#Df = [0,6.0,5.0,5.0,5.0,6.5,5.0,0,0,0] #for c dorian
Df = [0,6.5,7.0,5.0,6.5,6.5,6.5,0,0,0] #for D ionian 
#END OF USER INPUT VARIABLES 
###################################
'''
if key == 'C': dist_from_c = 48
elif key == 'C#': dist_from_c = 49
elif key == 'D': dist_from_c = 50
elif key == 'D#': dist_from_c = 51
elif key == 'E': dist_from_c = 52
elif key == 'F': dist_from_c = 53
elif key == 'F#': dist_from_c = 54
elif key == 'G': dist_from_c = 55
elif key == 'G#': dist_from_c = 56
elif key == 'A': dist_from_c = 57
elif key == 'A#': dist_from_c = 58
elif key == 'B': dist_from_c = 59
'''
if key == 'C': dist_from_c = 60
elif key == 'C#': dist_from_c = 61
elif key == 'D': dist_from_c = 62
elif key == 'D#': dist_from_c = 63
elif key == 'E': dist_from_c = 64
elif key == 'F': dist_from_c = 65
elif key == 'F#': dist_from_c = 66
elif key == 'G': dist_from_c = 67
elif key == 'G#': dist_from_c = 68
elif key == 'A': dist_from_c = 69
elif key == 'A#': dist_from_c = 70
elif key == 'B': dist_from_c = 71

#calculates frequencies for the holes
for i in mode:
	freq = math.pow(2, ((i+dist_from_c)/12.0 + math.log(C0,2)))
	Ff.append(freq)

Fend = math.pow(2, ((dist_from_c)/12.0 + math.log(C0,2)))

print "Target frequencies are: ", Ff

#anycalculator.com D example CM CONVERTED WORKING
'''
Vsound = 34500; #velocity of sound cm/second
Bore = 1.3;
wall = 0.1;
Demb = 1.0;
Df = [0,0.65,0.8,0.5,0.65,0.65,0.6,0,0,0]
Ff = [0,659.26,739.99,783.99,880,987.77,1108.73,0,0,0]
Fend = 587.33;
'''
#iotic.com 6-hole C5 mm WORKING
'''
Vsound = 345000; #velocity of sound mm/second
Bore = 19.0; #inside diameter of tube
wall = 1.25; # wall thickness of tube
Demb = 10.0; # embouchure hole diameter
Df = [0,10.0,9.5,7.0,9.0,8.5,8.0,0,0,0] # finger hole diameters
Df = [0,10.0,9.5,7.0,5.0,8.5,8.0,0,0,0]
Ff = [0,437.5,493.1,523.0,588.4,653.6,740.1,0,0,0] # finger hole note frequencies
Fend = 392.3 # all-holes-closed end-of-flute frequency
'''

#11wall-west.com default D inch WORKING 
'''
Vsound = 13584; #inch/second
Bore = 0.824;
wall = 0.113;
Demb = 0.500;
#Df = [0,0.375,0.375,0.3125,0.3125,0.4375,0.25,0,0,0];
Df = [0,0.25,0.4375,0.3125,0.3125,0.375,0.375,0,0,0];
#Ff = [0,554.37,493.88,440,392.00,369.99,329.63,0,0,0];
Ff = [0,329.63,369.99,392.00,440,493.88,554.37,0,0,0]; //low to high
Fend = 293.66;
'''



def te(n) :
	global holeCount, Df, Vsound, Ff, Xend, Xf, Xemb, Bore, wall, Demb, Df, Ff, Fend
	return (1.0*wall) + (0.75*Df[n])
# effective wall thickness, i.e. height of air column at open finger holes;
# air column extends out past end of hole 3/4 of the hole diameter

def C_c(n):
	global holeCount, Df, Vsound, Ff, Xend, Xf, Xemb, Bore, wall, Demb, Df, Ff, Fend
	return 0.25 * wall * (Df[n]/Bore)*(Df[n]/Bore);
# Closed hole for tone hole n.  The length of the vibrating air column is
# effectively increased by each closed tone hole which exists above the
# first open tone hole. Corrections must be added for each such closed tone
# tone hole to C_end, C_s, and C_o.


def C_end():
	global holeCount, Df, Vsound, Ff, Xend, Xf, Xemb, Bore, wall, Demb, Df, Ff, Fend
	return 0.6133 * Bore / 2;
# Calculates the distance from physical open end of flute to effective end of
# vibrating air column.  The vibrating air column ends beyond the end of the
# flute and C_end is always positive. NOTE: Closed hole corrections must be added to
# this value!

def C_s():
	global holeCount, Df, Vsound, Ff, Xend, Xf, Xemb, Bore, wall, Demb, Df, Ff, Fend
	return  te(1)/( (Df[1]/Bore)*(Df[1]/Bore) + te(1)/(Xend-Xf[1]) );
# Calculates the effective distance from the first ("single") tone hole to
# the end of the vibrating air column when only that hole is open.
# NOTE: closed hole corrections must be added to this value!

def C_o(n):
	global holeCount, Df, Vsound, Ff, Xend, Xf, Xemb, Bore, wall, Demb, Df, Ff, Fend
	return ((Xf[n-1]-Xf[n])/2)*(math.sqrt(1+4*(te(n)/(Xf[n-1]-Xf[n]))*(Bore/Df[n])*(Bore/Df[n]))-1);
# Calculates the effective distance from the second and subsequent tone holes
# to the end of the vibrating air column when all holes below are open.
# NOTE: closed hole corrections must be added to this value!
# NOTE: the value of this correction is invalid if the frequency of the note
# played is above the cutoff frequency f_c.

def C_emb():
	global holeCount, Df, Vsound, Ff, Xend, Xf, Xemb, Bore, wall, Demb, Df, Ff, Fend
	return (Bore/Demb)*(Bore/Demb)*10.84*wall*Demb/(1.0*Bore + 2*wall);
# C_emb = distance from theoretical start of air column to center of embouchure hole;
# the air column effectively extends beyond the blow hole center by this distance.
# (the cork face should be about 1 to 1.5 embouchure diameters from emb. center)
#C_emb := (Bore/Demb)*(Bore/Demb)*(wall+0.75*Demb); // per spreadsheet
#C_emb := (Bore/Demb)*(Bore/Demb)*(Bore/2 + wall + 0.6133*Demb/2); // an alternative
#C_emb := (Bore/Demb)*(Bore/Demb)*10.84*wall*Demb/(Bore + 2*wall); // kosel's empirical fit

def f_c(n):
	global holeCount, Df, Vsound, Ff, Xend, Xf, Xemb, Bore, wall, Demb, Df, Ff, Fend
	Pi = 3.14159
	#print "cutoff: ", n
	try: 
		cutoff = Vsound/(2.0*Pi)*(Df[n]/Bore)*1/math.sqrt(te(n)*(Xf[n-1]-Xf[n]));
		return cutoff
	except:
		print "hole ", n, " cutoff calculation failed"
		return 
# Calculates the cutoff frequency above which the open hole correction
# is not valid.  Instrument should be designed so that all second register
# notes are well below this frequency.

def FindLocations2():
# This is a non-iterative procedure equivalent to the above procedure.  It involves use
# of quadratic solutions of the Benade equations obtained by "simple but tedious algebraic
# manipulation".
	global holeCount, Df, Vsound, Ff, Xend, Xf, Xemb, Bore, wall, Demb, Df, Ff, Fend

	# find end location...
	Xend = Vsound * 0.5 / Fend;  # uncorrected location
	Xend = Xend - C_end();  # subtract end correction
	print "Xend: ", Xend
	for i in range(1,holeCount+1):
		Xend = Xend - C_c(i);  # subtract closed hole corrections
	

	# find first finger hole location
	L = Vsound * 0.5 / Ff[1];
	for i in range(2, holeCount+1):
		L = L - C_c(i);  # subtract closed hole corrections
	
	a = (Df[1]/Bore)*(Df[1]/Bore); 
	b = -(Xend + L)*(Df[1]/Bore)*(Df[1]/Bore); 
	c = Xend * L * (Df[1]/Bore)*(Df[1]/Bore) + te(1)*(L-Xend);
	Xf[1] = ( -b - math.sqrt((b*b) - 4*a*c) ) / (2*a);

	#find subsequent finger hole locations
	if(holeCount >= 2):
		for holeNum in range(2,holeCount+1):
			L = Vsound * 0.5 / Ff[holeNum]
			if (holeNum < holeCount):
				for i in range(holeNum,holeCount+1):
					L = L - C_c(i);
			a = 2;
			b = - Xf[holeNum-1] - 3*L + te(holeNum)*(Bore/Df[holeNum])*(Bore/Df[holeNum]);
			c = Xf[holeNum-1]*(L - te(holeNum)*(Bore/Df[holeNum])*(Bore/Df[holeNum])) + (L*L);
			try:
				Xf[holeNum] = ( -b - math.sqrt((b*b) - 4*a*c) ) / (2*a);
				print holeNum, ": location calc passed"
			except:
				print holeNum, ": location calc failed"
		

	# set embouchure hole location
	Xemb = C_emb();

FindLocations2();
#print "Xend: ", Xend
#print Xemb
#print Xf[6]

#distance from end of flute
resultEmb = .001*round(1000*(Xend-Xemb));
result6 = .001*round(1000*(Xend-Xf[6]));
result5 = .001*round(1000*(Xend-Xf[5]));
result4 = .001*round(1000*(Xend-Xf[4]));
result3 = .001*round(1000*(Xend-Xf[3]));
result2 = .001*round(1000*(Xend-Xf[2]));
result1 = .001*round(1000*(Xend-Xf[1]));
resultEnd = .001*round(1000*(Xend-Xend));

print "hole distances from end of flute: "
print(resultEmb,result6,result5,result4,result3,result2,result1,resultEnd)

if result6-result5 > 250: print "hole 6 to hole 5 distance might be too big"
if result5-result4 > 250: print "hole 5 to hole 4 distance might be too big"
if result4-result3 > 250: print "hole 4 to hole 3 distance might be too big"
if result3-result2 > 250: print "hole 3 to hole 2 distance might be too big"
if result2-result1 > 250: print "hole 2 to hole 1 distance might be too big"

#test values
'''
resultEmb = 410.1
result6 = 250.5
result5 = 217.8
result4 = 189.1
result3 = 152.8
result2 = 132.9
result1 = 86.6
resultEnd = 48

Demb = 10
Df = [0,8,8.5,9,7,9.5,10,5.5]

Bore = 19
wall = 1.25
'''
#end of test values 

#test for cutoff values (for second octave)
for n in range(2, holeCount+1): 
	if Ff[n]*2.1 < f_c(n):
		print "HOLE ", n, " is okay. ", Ff[n], f_c(n)
	else:
		print "HOLE ", n, " is too small. ", Ff[n], f_c(n)
		Df[n] = f_c(n) * (2*3.14159)/Vsound * math.sqrt(te(n)*(Xf[n-1]-Xf[n])) * Bore
		print "HOLE ", n, " new diameter is ", Df[n], Ff[n], f_c(n)



# this part turns the parameters into openSCAD code with the solidpython library
external_diameter = Bore + 2*wall
embToCork = 0.5 * Demb + 0.2*Bore
cork_depth = 0.4 * Bore
overhang = 1.5 * external_diameter
total_length = resultEmb + embToCork + cork_depth + overhang


exterior = cylinder(r=external_diameter/2, h=total_length)
interior = cylinder(r=Bore/2, h=total_length)
embouchure = right(resultEmb)(cylinder(r=Demb/2, h=external_diameter))
h6 = right(result6)(cylinder(r=Df[6]/2, h=external_diameter))
h5 = right(result5)(cylinder(r=Df[5]/2, h=external_diameter))
h4 = right(result4)(cylinder(r=Df[4]/2, h=external_diameter))
h3 = right(result3)(cylinder(r=Df[3]/2, h=external_diameter))
h2 = right(result2)(cylinder(r=Df[2]/2, h=external_diameter))
h1 = right(result1)(cylinder(r=Df[1]/2, h=external_diameter))

cork = up(resultEmb + embToCork) (cylinder(r=Bore/2, h = cork_depth))

rotated_holes = rotate(a=-90, v=FORWARD_VEC)(embouchure + h6 + h5 + h4 + h3 + h2 + h1)

whole_flute = exterior - interior + cork - rotated_holes

#cut at embouchure 
cut = whole_flute - up(resultEmb)(cylinder(r=external_diameter/2+0.1, h=total_length-resultEmb+0.1))

recorder_depth = 81.5 
depth_to_stopper = 23.5
difference = 81.5 - 23.5
recorder_attachment = cut - up(total_length-(total_length-resultEmb+difference))(cylinder(r=external_diameter/2+0.1, h=total_length-resultEmb+difference+0.1))

print(scad_render(recorder_attachment))













