def Chisholm_Y (Array, PressureGradient_lo, PressureGradient_go, Y_name = 'Y [-]'):
    '''Calculation of Chisholm Y parameter.
    Inputs are: Array - final table, PressureGradient_lo - pressure gradient of liquid only phase [Pa/m], PressureGradient_go - pressure gradient of gas only phase [Pa/m].'''
    import numpy as np
    Array[Y_name] = np.sqrt(PressureGradient_go/PressureGradient_lo)
    return Array[Y_name]
