def Haraguchi_1993 (Array, rho_l, rho_g, DynVisc_g, MassQual, MassFlux_tp, X_pred, CrossSection, Gconst, TPM_name = 'phi^2_pred_Haraguchi_1993_g [-]', HM_name = 'Dp/dz_pred_Haraguchi_1993 [Pa/m]'):
    '''Calculation of Haraguchi et al. (1993) model for two phase flow multiplier - gas.
    Inputs are: Array - final table, rho_l - Density of the liquid phase [kg/m^3], rho_g - Density of the gas phase [kg/m^3], DynVisc_g - Dynamic viscosity of the gas [Pa*s], MassQual - mass quality [-], MassFlux_tp - Total mass flux [kg/m^2/s], X_pred - Lockhart and Martinelli parameter defined by power law [-], CrossSection - Cross section of the tube [m^2], Gconst - gravitational constant acceleration [m/s^2].'''    
    import numpy as np
    De = np.sqrt((4*CrossSection)/np.pi)
    Re_e_g = (MassFlux_tp * De * MassQual) / DynVisc_g
    f_e_g = 0.046 * Re_e_g**(-0.2)
    phi = 1.1 + 1.3 * (X_pred * MassFlux_tp / (Gconst * De * rho_g * (rho_l - rho_g))**0.5 )**0.35
    Dp_dz = phi**2 * (2 * f_e_g * (MassFlux_tp*MassQual)**2)/(rho_g * De)
    
    Array[TPM_name] = phi**2
    Array[HM_name]  = Dp_dz
    
    return Array[TPM_name] ,Array[HM_name]
