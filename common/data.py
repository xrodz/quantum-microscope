# Data file

#------------------------------------------------------------------------------------------------------
# DATA FOR ATOMS AND ORBITALS
# The configuration of atoms and orbitals uses multiequation solves to calculate positions of various
# particles that affect each other.  This data file uses pre-calculated values found in arrays here.
# The raw data may be downloaded from https://energywavetheory.com/equations/summary-of-calculations/
# TODO: The calculations may be moved to Blender/Python if multiequation solvers can be applied, making this file unnecessary in the future.
# TODO: Most calculations stop at 12 electrons because determining constructive wave interference approximation yields increasing errors - can be corrected with a simulator knowing distances
#------------------------------------------------------------------------------------------------------

import bpy

#------------------------------------------------------------------------------------------------------
# DETERMINE ATOM TYPE AND ARRAY
# Select the correct table if it is an ion, and determine the ratio used for orbital distances (orbital_ratio) and amplitude factor for wave interference (amplitude_ratio)
# TODO: This could be made more efficient, but this data file may be replaced with a multiequation solver anyway so that tables do not need to be use_max_distance
#------------------------------------------------------------------------------------------------------

def get_orbital_array(electrons, atom_name):
    atom_name = atom_name
    if electrons == 1:
        orbital_ratio = ion_atom_1
        amplitude_ratio = amp_atom_1
    elif electrons == 2:
        orbital_ratio = ion_atom_2
        amplitude_ratio = amp_atom_2
    elif electrons == 3:
        orbital_ratio = ion_atom_3
        amplitude_ratio = amp_atom_3
    elif electrons == 4:
        orbital_ratio = ion_atom_4
        amplitude_ratio = amp_atom_4
    elif electrons == 5:
        orbital_ratio = ion_atom_5
        amplitude_ratio = amp_atom_5
    elif electrons == 6:
        orbital_ratio = ion_atom_6
        amplitude_ratio = amp_atom_6
    elif electrons == 7:
        orbital_ratio = ion_atom_7
        amplitude_ratio = amp_atom_7
    elif electrons == 8:
        orbital_ratio = ion_atom_8
        amplitude_ratio = amp_atom_8
    elif electrons == 9:
        orbital_ratio = ion_atom_9
        amplitude_ratio = amp_atom_9
    elif electrons == 10:
        orbital_ratio = ion_atom_10
        amplitude_ratio = amp_atom_10
    elif electrons == 11:
        orbital_ratio = ion_atom_11
        amplitude_ratio = amp_atom_11
    elif electrons == 12:
        orbital_ratio = ion_atom_12
        amplitude_ratio = amp_atom_12
    else:
        orbital_ratio = neutral_atom   # Default to neutral atom if ion table is not found.  This is incorrect data, but it will say atom not supported
        amplitude_ratio = amp_neutral
        atom_name = "Atom not supported"
    return orbital_ratio, amplitude_ratio, atom_name


#------------------------------------------------------------------------------------------------------
# ATOM SYMBOLS
# An array of atom symbols
# TODO: Only supports up to calcium as data file supports s and p orbitals only.  Need to expand list.
#------------------------------------------------------------------------------------------------------

atoms = ["Atom", "H", "He", "Li", "Be", "B", "C", "N",	"O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca" ]


#------------------------------------------------------------------------------------------------------
# ORBITAL FILL SEQUENCE
# Fill order of electrons in 1s, 2s, 2p, 3s, 3p and 4s shells.
# TODO: Only supports the sequence to 20 electrons currently as only up to calcium supported.
#------------------------------------------------------------------------------------------------------

electron_sequence = [ 2, 2, 6, 2, 6, 2 ]


#------------------------------------------------------------------------------------------------------
# ORBITAL DISTANCES
# Orbital distances relative to the Bohr radius for neutral and ion atoms.
# Precalculated using Math-cad simultaneous equation solver.  From https://energywavetheory.com/atoms/calculations-atoms/
# TODO: Currently supports up to calcium. May be expanded here as a table or replaced with direct equation solver in Python
#------------------------------------------------------------------------------------------------------

# Neutral atom orbital distances
neutral_atom =    [ ["1s",1.000,0.571,0.397,0.285,0.226,0.185,0.157,0.137,0.121,0.108,0.098,0.089,0.082,0.076,0.071,0.066,0.062,0.058,0.055,0.052],
                    ["2s",0.000,0.000,3.272,2.096,1.643,1.294,1.066,0.905,0.786,0.695,0.592,0.518,0.463,0.418,0.381,0.351,0.325,0.302,0.282,0.264],
                    ["2p",0.000,0.000,0.000,0.000,1.410,1.143,0.960,0.828,0.727,0.648,0.560,0.494,0.444,0.403,0.369,0.340,0.316,0.295,0.275,0.259],
                    ["3s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,3.539,2.623,2.676,2.219,1.894,1.652,1.465,1.316,1.147,1.023],
                    ["3p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,1.797,1.571,1.398,1.260,1.148,1.055,0.949,0.866],
                    ["4s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,3.674,3.131] ]

# Ionized atom orbital distances (appending number is the number of electrons in the atom (e.g. ion_atom_1 is elements from H to Ca with one electron))
ion_atom_1 =    [ [ "1s",0.000,0.500,0.333,0.250,0.200,0.167,0.143,0.125,0.111,0.100,0.091,0.083,0.077,0.071,0.067,0.063,0.059,0.056,0.053,0.050 ] ]

ion_atom_2 =    [ [ "1s",0.000,0.571,0.364,0.267,0.211,0.174,0.148,0.129,0.114,0.103,0.093,0.085,0.078,0.073,0.068,0.063,0.060,0.056,0.053,0.051 ] ]

ion_atom_3 =    [ [ "1s",0.000,0.000,0.397,0.286,0.223,0.183,0.155,0.134,0.118,0.106,0.096,0.087,0.080,0.074,0.069,0.065,0.061,0.057,0.054,0.051 ],
                  [ "2s",0.000,0.000,3.272,1.746,1.203,0.921,0.747,0.628,0.542,0.477,0.426,0.385,0.351,0.323,0.299,0.278,0.260,0.244,0.230,0.217 ] ]

ion_atom_4 =    [ [ "1s",0.000,0.000,0.000,0.285,0.223,0.183,0.155,0.134,0.118,0.106,0.096,0.087,0.080,0.074,0.069,0.065,0.061,0.057,0.054,0.051 ],
                  [ "2s",0.000,0.000,0.000,2.096,1.345,0.998,0.795,0.661,0.567,0.496,0.441,0.397,0.361,0.331,0.305,0.284,0.265,0.248,0.234,0.221 ] ]

ion_atom_5 =    [ [ "1s",0.000,0.000,0.000,0.000,0.226,0.185,0.157,0.136,0.120,0.107,0.097,0.088,0.081,0.075,0.070,0.065,0.061,0.058,0.055,0.052 ],
                  [ "2s",0.000,0.000,0.000,0.000,1.643,1.146,0.885,0.722,0.610,0.528,0.466,0.417,0.378,0.345,0.317,0.294,0.274,0.256,0.241,0.227 ],
                  [ "2p",0.000,0.000,0.000,0.000,1.410,1.041,0.824,0.682,0.582,0.508,0.450,0.405,0.367,0.336,0.310,0.288,0.268,0.252,0.237,0.223 ] ]

ion_atom_6 =    [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.185,0.157,0.136,0.120,0.107,0.097,0.089,0.081,0.075,0.070,0.065,0.061,0.058,0.055,0.052 ],
                  [ "2s",0.000,0.000,0.000,0.000,0.000,1.294,0.965,0.773,0.645,0.554,0.486,0.433,0.390,0.355,0.326,0.302,0.280,0.262,0.246,0.232 ],
                  [ "2p",0.000,0.000,0.000,0.000,0.000,1.143,0.887,0.725,0.613,0.531,0.468,0.419,0.379,0.346,0.318,0.295,0.275,0.257,0.241,0.228 ] ]

ion_atom_7 =    [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.157,0.137,0.120,0.108,0.097,0.089,0.082,0.076,0.070,0.066,0.062,0.058,0.055,0.052 ],
                  [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,1.066,0.833,0.685,0.583,0.508,0.450,0.404,0.367,0.336,0.310,0.287,0.268,0.251,0.236 ],
                  [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.960,0.773,0.647,0.556,0.488,0.434,0.392,0.356,0.327,0.302,0.281,0.263,0.246,0.232 ] ]

ion_atom_8 =    [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.137,0.121,0.108,0.098,0.089,0.082,0.076,0.070,0.066,0.062,0.058,0.055,0.052 ],
                  [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.905,0.732,0.615,0.532,0.468,0.419,0.379,0.346,0.318,0.294,0.274,0.256,0.241 ],
                  [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.828,0.684,0.584,0.509,0.451,0.405,0.368,0.336,0.310,0.288,0.268,0.252,0.237 ] ]

ion_atom_9 =    [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.121,0.108,0.098,0.089,0.082,0.076,0.071,0.066,0.062,0.058,0.055,0.052 ],
                  [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.786,0.652,0.558,0.489,0.435,0.392,0.356,0.327,0.302,0.281,0.262,0.246 ],
                  [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.727,0.614,0.532,0.469,0.419,0.379,0.346,0.319,0.295,0.275,0.257,0.241 ] ]

ion_atom_10 =    [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.108,0.098,0.089,0.082,0.076,0.071,0.066,0.062,0.058,0.055,0.052 ],
                   [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.695,0.588,0.511,0.452,0.405,0.368,0.336,0.310,0.288,0.268,0.251 ],
                   [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.648,0.557,0.488,0.435,0.392,0.357,0.327,0.302,0.281,0.263,0.246 ] ]

ion_atom_11 =   [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.098,0.089,0.082,0.076,0.071,0.066,0.062,0.058,0.055,0.052 ],
                  [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.592,0.516,0.457,0.410,0.371,0.340,0.313,0.290,0.270,0.253 ],
                  [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.560,0.492,0.439,0.395,0.300,0.330,0.305,0.283,0.265,0.248 ],
                  [ "3s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,3.539,2.225,1.689,1.380,1.177,1.029,0.916,0.827,0.754,0.693 ] ]

ion_atom_12 =   [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.089,0.082,0.076,0.071,0.066,0.062,0.058,0.055,0.052 ],
                  [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.518,0.460,0.413,0.374,0.343,0.316,0.292,0.273,0.255 ],
                  [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.494,0.441,0.398,0.363,0.333,0.307,0.286,0.267,0.250 ],
                  [ "3s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,2.623,1.880,1.496,1.255,1.085,0.959,0.861,0.781,0.716 ] ]


#------------------------------------------------------------------------------------------------------
# AMPLITUDE FACTORS
# Amplitude factors which are used to approximate constructive wave interference relative to a single proton and a single electron for neutral and ion atoms.
# Precalculated using amplitude factor equations for orbitals - from EWT: https://energywavetheory.com/atoms/calculations-amplitude-factors/
# TODO: By knowing exact electron positions in an atom, true wave interference can be calculated instead of approximated, replacing the need for this section.
#------------------------------------------------------------------------------------------------------

# Note the 3p and 4s orbitals are calculated in EWT, but beyond 12 electrons the accuracy diminishes and is often greater than 10%. So they have been excluded.
amp_neutral = [ [ "1s",1.000,1.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000 ],
                [ "2s",0.000,0.000,1.306,1.477,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000 ],
                [ "2p",0.000,0.000,0.000,0.000,0.855,0.937,1.021,0.854,0.938,1.022,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000 ],
                [ "3s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,1.283,1.381,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000 ],
                [ "3p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000 ],
                [ "4s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000 ] ]

amp_atom_1 =  [ [ "1s",0.000,2.000,3.000,4.000,5.000,6.000,7.000,8.000,9.000,10.00,11.00,12.00,13.00,14.00,15.00,16.00,17.00,18.00,19.00,20.00 ] ]

amp_atom_2 =  [ [ "1s",0.000,1.000,2.000,3.000,4.000,5.000,6.000,7.000,8.000,9.000,10.00,11.00,12.00,13.00,14.00,15.00,16.00,17.00,18.00,19.00 ] ]

amp_atom_3 =  [ [ "1s",0.000,0.000,1.889,3.622,5.363,7.098,8.839,10.60,12.36,14.08,15.81,17.62,19.38,21.14,22.87,24.54,26.30,28.16,29.89,31.71 ],
                [ "2s",0.000,0.000,1.306,2.306,3.306,4.306,5.306,6.306,7.306,8.306,9.306,10.31,11.31,12.31,13.31,14.31,15.31,16.31,17.31,18.31 ] ]

amp_atom_4 =  [ [ "1s",0.000,0.000,0.000,2.632,4.363,6.098,7.839,9.597,11.36,13.08,14.81,16.62,18.38,20.14,21.87,23.54,25.30,27.16,28.89,30.71 ],
                [ "2s",0.000,0.000,0.000,1.477,2.477,3.477,4.477,5.477,6.477,7.477,8.477,9.477,10.48,11.48,12.48,13.48,14.48,15.48,16.48,17.48 ] ]

amp_atom_5 =  [ [ "1s",0.000,0.000,0.000,0.000,3.319,5.054,6.777,8.515,10.25,12.01,13.73,15.52,17.26,19.00,20.71,22.54,24.30,25.93,27.64,29.42 ],
                [ "2s",0.000,0.000,0.000,0.000,1.609,2.609,3.609,4.609,5.609,6.609,7.609,8.609,9.609,10.61,11.61,12.61,13.61,14.61,15.61,16.61 ],
                [ "2p",0.000,0.000,0.000,0.000,0.855,1.855,2.855,3.855,4.855,5.855,6.855,7.855,8.855,9.855,10.85,11.85,12.85,13.85,14.85,15.85 ] ]

amp_atom_6 =  [ [ "1s",0.000,0.000,0.000,0.000,0.000,4.054,5.777,7.515,9.250,11.01,12.73,14.43,16.26,18.00,19.71,21.54,23.30,24.93,26.64,28.42 ],
                [ "2s",0.000,0.000,0.000,0.000,0.000,1.773,2.773,3.773,4.773,5.773,6.773,7.773,8.773,9.773,10.77,11.77,12.77,13.77,14.77,15.77 ],
                [ "2p",0.000,0.000,0.000,0.000,0.000,0.937,1.937,2.937,3.937,4.937,5.937,6.937,7.937,8.937,9.937,10.94,11.94,12.94,13.94,14.94 ] ]

amp_atom_7 =  [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,4.777,6.474,8.250,9.944,11.73,13.43,15.15,16.87,18.71,20.36,22.10,23.93,25.64,27.42 ],
                [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,1.938,2.938,3.938,4.938,5.938,6.938,7.938,8.938,9.938,10.94,11.94,12.94,13.94,14.94 ],
                [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,1.021,2.021,3.021,4.021,5.021,6.021,7.021,8.021,9.021,10.02,11.02,12.02,13.02,14.02 ] ]

amp_atom_8 =  [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,5.474,7.198,8.944,10.65,12.43,14.15,15.87,17.71,19.36,21.10,22.93,24.64,26.42 ],
                [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,2.105,3.105,4.105,5.105,6.105,7.105,8.105,9.105,10.10,11.10,12.10,13.10,14.10 ],
                [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.854,1.854,2.854,3.854,4.854,5.854,6.854,7.854,8.854,9.854,10.85,11.85,12.85 ] ]

amp_atom_9 =  [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,6.198,7.944,9.653,11.43,13.15,14.87,16.56,18.36,20.10,21.93,23.64,25.42 ],
                [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,2.272,3.272,4.272,5.272,6.272,7.272,8.272,9.272,10.27,11.27,12.27,13.27 ],
                [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.938,1.938,2.938,3.938,4.938,5.938,6.938,7.938,8.938,9.938,10.94,11.94 ] ]

amp_atom_10 = [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,6.944,8.653,10.43,12.15,13.87,15.56,17.36,19.10,20.93,22.64,24.42 ],
                [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,2.439,3.439,4.439,5.439,6.439,7.439,8.439,9.439,10.44,11.44,12.44 ],
                [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,1.022,2.022,3.022,4.022,5.022,6.022,7.022,8.022,9.022,10.02,11.02 ] ]

amp_atom_11 = [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,7.653,9.427,11.15,12.87,14.56,16.36,18.10,19.93,21.64,23.42 ],
                [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,2.689,3.689,4.689,5.689,6.689,7.689,8.689,9.689,10.69,11.69 ],
                [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,1.393,2.393,3.393,4.393,5.393,6.393,7.393,8.393,9.393,10.39 ],
                [ "3s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,1.283,2.283,3.283,4.283,5.283,6.283,7.283,8.283,9.283,10.28 ] ]

amp_atom_12 = [ [ "1s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,8.427,10.15,11.87,13.56,15.36,17.10,18.93,20.64,22.42 ],
                [ "2s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,2.931,3.931,4.931,5.931,6.931,7.931,8.931,9.931,10.93 ],
                [ "2p",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,1.512,2.512,3.512,4.512,5.512,6.512,7.512,8.512,9.512 ],
                [ "3s",0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,1.381,2.381,3.381,4.381,5.381,6.381,7.381,8.381,9.381 ] ]
