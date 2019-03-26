def Tran_2000 (Array, rho_l, rho_g, Chisholm_Y, MassQual, D_int, SurfaceTension, Gconst, TPM_name = 'phi^2_pred_Tran_2000_lo [-]'):
    '''Calculation of Tran et al. (2000) model for two phase flow multiplier - loquid only.
    Inputs are: Array - final table, rho_l - Density of the liquid phase, rho_g - Density of the gas phase, Chisholm_Y - Chisholm Y parameter, MassQual - mass quality, D_int - internal diameter of the tube, SurfaceTension - surface tension of the fluid, Gconst - gravitational constant acceleration.'''    
    
    Nconf = (SurfaceTension/(Gconst * (rho_l - rho_g)))**0.5 / D_int #confinment number
    phi = 1 + (Chisholm_Y**2 - 1) * (Nconf * (MassQual * (1 - MassQual))**0.875 + MassQual**1.75)
    Array[TPM_name] = phi
       
    return Array[TPM_name] 
