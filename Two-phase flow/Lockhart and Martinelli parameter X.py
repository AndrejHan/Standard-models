def Lockhart_Martinelli_1949 (Array, PressureGradient_l, PressureGradient_g, MassQuality, Density_l, Density_g, DynamicViscosity_l, DynamicViscosity_g, LM_name = 'X [-]'):
    '''Calculation of Lockhart and Martinelli parameter X.
    Inputs are: Array - final table, PressureGradient_l - pressure gradient of liquid phase, PressureGradient_g - pressure gradient of gas phase.'''
    import numpy as np
    
    Array[LM_name] = np.sqrt(PressureGradient_l/PressureGradient_g)
    return Array[LM_name]
