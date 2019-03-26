def MullerSteinhagen_Heck_1986(Array, Chisholm_Y, MassQual, TPM_name = 'phi^2_pred_MullerSteinhagen_Heck_1986_lo [-]'):
    '''Calculation of Muller-Steinhagen and Heck (1986) model for two phase flow multiplier - liquid.
    Inputs are: Array - final table, Chisholm_Y - Y two pase parameter defined by Chisholm, MassQual - mass quality.'''    
    phi = Chisholm_Y**2 * MassQual**3 + (1 - MassQual)**(1/3) * (1 + 2*MassQual*(Chisholm_Y**2 - 1))
    Array[TPM_name] = phi
    return Array[TPM_name]
