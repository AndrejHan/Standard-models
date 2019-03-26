def Friedel_1979 (Array, rho_l, rho_g, rho_tp, DynVisc_l, DynVisc_g, f_lo, f_go, MassQual, MassFlux_tp, D_int, SurfaceTension, Gconst, TPM_name = 'phi^2_pred_Friedel_1979_lo [-]'):
    '''Calculation of Friedel et al. (1979) model for two phase flow multiplier - loquid only.
    Inputs are: Array - final table, rho_l - Density of the liquid phase [kg/m^3], rho_g - Density of the gas phase [kg/m^3], rho_tp - Density of the two phase flow [kg/m^3], DynVisc_l - Dynamic viscosity of the liquid [Pa*s], DynVisc_g - Dynamic viscosity of the gas [Pa*s], MassQual - mass quality [-], MassFlux_tp - Total mass flux [kg/m^2/s], D_int - internal diameter of the tube [m], SurfaceTension - surface tension of the fluid [N/m], Gconst - gravitational constant acceleration [m/s^2].'''    
  
    FroudeN = MassFlux_tp**2 / (Gconst * D_int * rho_tp**2)
    WeberN = MassFlux_tp**2 * D_int *(SurfaceTension * rho_tp) 
    phi = (1-MassQual)**2 + MassQual**2 * (rho_l*f_go)/(rho_g*f_lo) + (3.24* MassQual**0.78 * (1-MassQual)**0.224 * (rho_l/rho_g)**0.91) / (FroudeN**0.045 * WeberN**0.035 * (DynVisc_g/DynVisc_l)**(-0.19) * (1 - DynVisc_g/DynVisc_l)**(-0.7))
        
    Array[TPM_name] = phi
       
    return Array[TPM_name]
