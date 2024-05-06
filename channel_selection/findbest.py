import collections

# quick script to identify some of the best channels 

bl = [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 16, 17, 19, 20, 21, 23, 24, 26, 27, 28, 29, 30, 33, 34, 36, 37, 38, 39, 41, 42, 46, 47, 50, 54, 57, 58, 66, 67, 69, 70, 71, 72, 73, 80, 81, 83, 84, 91, 92, 97, 98, 100, 107, 108, 110, 123]

ml = [0, 1, 9, 11, 12, 13, 23, 25, 32, 33, 35, 36, 37, 39, 41, 43, 45, 46, 47, 49, 51, 53, 54, 55, 61, 64, 65, 68, 74, 76, 77, 82, 84, 85, 86, 92, 94, 98, 100, 101, 104, 109, 111, 117, 120, 123, 124, 125]

a = [1, 2, 7, 9, 10, 11, 15, 17, 18, 20, 21, 22, 23, 24, 27, 33, 34, 36, 37, 38, 39, 40, 46, 48, 49, 52, 53, 54, 56, 60, 72, 77, 79, 80, 90, 97, 103, 105, 106, 108, 114, 120, 124]

e = [1, 2, 3, 4, 8, 9, 11, 12, 20, 23, 24, 25, 26, 27, 30, 31, 33, 36, 39, 40, 50, 51, 52, 56, 59, 60, 63, 64, 67, 75, 78, 79, 85, 87, 88, 89, 90, 91, 93, 94, 95, 99, 102, 103, 104, 111, 112, 114, 115]
print(len(a))
print(len(bl))
print(len(ml))
print(len(e))

s = ml + bl + a + e
s = set(s)
print(len(s))
print(s)

# union all 3 lists
r = collections.Counter(ml) & collections.Counter(bl) & collections.Counter(a)
i = list(r.elements())
print(len(i))
print(i)

electrode_names = [
    "FP1", "FPz", "FP2", "AFp1", "AFPz", "AFp2", "AF7", "AF3", "AF4", "AF8",
    "AFF5h", "AFF1h", "AFF2h", "AFF6h", "F9", "F7", "F5", "F3", "F1", "Fz",
    "F2", "F4", "F6", "F8", "F10", "FFT9h", "FFT7h", "FFC5h", "FFC3h", "FFC1h",
    "FFC2h", "FFC4h", "FFC6h", "FFT8h", "FFT10h", "FT9", "FT7", "FC5", "FC3",
    "FC1", "FCz", "FC2", "FC4", "FC6", "FT8", "FT10", "FTT9h", "FTT7h", "FCC5h",
    "FCC3h", "FCC1h", "FCC2h", "FCC4h", "FCC6h", "FTT8h", "FTT10h", "T7", "C5",
    "C3", "C1", "Cz", "C2", "C4", "C6", "T8", "TTP7h", "CCP5h", "CCP3h", "CCP1h",
    "CCP2h", "CCP4h", "CCP6h", "TTP8h", "TP9", "TP7", "CP5", "CP3", "Cpz", "CP4",
    "CP6", "TP8", "TP10", "TPP9h", "TPP7h", "CPP5h", "CPP3h", "CPP1h", "CPP2h",
    "CPP4h", "CPP6h", "TPP8h", "TPP10h", "P9", "P7", "P5", "P3", "P1", "Pz", "P2",
    "P4", "P6", "P8", "P10", "PPO9h", "PPO5h", "PPO1h", "PPO2h", "PPO6h", "PPO10h",
    "PO9", "PO7", "PO3", "POz", "PO4", "PO8", "PO10", "POO9h", "POO1", "POO2",
    "POO10h", "O1", "Oz", "O2", "OI1h", "OI2h", "I1", "Iz", "I2"
]

for j in i:
    print(electrode_names[j])
