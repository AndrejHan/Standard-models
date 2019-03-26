def Tran_2000 (Array, rho_l, rho_g, Chisholm_Y, MassQual, D_int, SurfaceTension, Gconst, TPM_name = 'phi^2_pred_Tran_2000_lo [-]'):
    '''Calculation of Tran et al. (2000) model for two phase flow multiplier - loquid only.
    Inputs are: Array - final table, rho_l - Density of the liquid phase [kg/m^3], rho_g - Density of the gas phase [kg/m^3], Chisholm_Y - Chisholm Y parameter [-], MassQual - mass quality [-], D_int - internal diameter of the tube [m], SurfaceTension - surface tension of the fluid [N/m], Gconst - gravitational constant acceleration [m/s^2].'''    
    
    Nconf = (SurfaceTension/(Gconst * (rho_l - rho_g)))**0.5 / D_int #confinment number
    phi = 1 + (Chisholm_Y**2 - 1) * (Nconf * (MassQual * (1 - MassQual))**0.875 + MassQual**1.75)
    Array[TPM_name] = phi
       
    return Array[TPM_name] 
