def Souza_Pimenta_1995(Array, MassQual, rho_l, rho_g, DynVisc_l, DynVisc_g, TPM_name = 'phi^2_pred_Souza_Pimenta_1995_lo [-]'):
    '''Calculation of Souza and Pimenta (1995) model for two phase flow multiplier - liquid.
    Inputs are: Array - final table, MassQual - mass quality, rho_l - density of the liquid, rho_g - density of the gas, DynVisc_l - Dynamic viscosity of liquid, DynVisc_g - Dynamic viscosity of gas.'''
    Gama = (rho_l/rho_g)**0.5 * (DynVisc_g/DynVisc_l)**0.125
    Xtt = 1/Gama *((1-MassQual)/MassQual)**0.875
    phi = 1 + (Gama**2 - 1)*MassQual**1.75 * (1+ 0.9524 * Gama * Xtt**0.4126)
    Array[TPM_name]  = phi
    return Array[TPM_name]
