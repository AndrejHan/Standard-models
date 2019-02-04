def f_exp(Array, Diameter_internal, Density, PressureGradient, MassFlux, f_name = 'f_exp [-]' ):
    '''Calculation of experimental friction factor (by Fanning).
    Inputs are: Array - final table, Diameter_internal - internal diameter of the tube, Density - density of the fluid, PressureGradient - in the flow duct, MassFlux - of the relative flow.'''
    Array[f_name] = PressureGradient * Diameter_internal * Density / (2 * MassFlux**2)
    return Array[f_name]
