def Lockhart_Martinelli_1949 (Array, PressureGradient_l, PressureGradient_g, MassQuality, Density_l, Density_g, DynamicViscosity_l, DynamicViscosity_g, f_usage = True, LM_name = 'X [-]'):
    '''Calculation of Lockhart and Martinelli parameter.
    Inputs are: Array - final table, PressureGradient_l - pressure gradient of liquid phase [Pa/m], PressureGradient_g - pressure gradient of gas phase [Pa/m].'''
    import numpy as np
    if f_usage == True:
            Array[LM_name] = np.sqrt(PressureGradient_l/PressureGradient_g)
            return Array[LM_name]
    
    elif f_usage == False: #power law
            Array[LM_name] = ((1-MassQuality)/MassQuality)**0.9 * (Density_g/Density_l)**0.5 * (DynamicViscosity_l/DynamicViscosity_g)**0.1
            return Array[LM_name] 
