def Friedel_1979 (Array, rho_l, rho_g, rho_tp, DynVisc_l, DynVisc_g, f_lo, f_go, MassQual, MassFlux_tp, D_int, SurfaceTension, Gconst, TPM_name = 'phi^2_pred_Friedel_1979_lo [-]'):
    '''Calculation of Friedel et al. (1979) model for two phase flow multiplier - loquid only.
    Inputs are: Array - final table, rho_l - Density of the liquid phase, rho_g - Density of the gas phase, rho_tp - Density of the two phase flow, DynVisc_l - Dynamic viscosity of the liquid, DynVisc_g - Dynamic viscosity of the gas, MassQual - mass quality, MassFlux_tp - Total mass flux, D_int - internal diameter of the tube, SurfaceTension - surface tension of the fluid, Gconst - gravitational constant acceleration.'''    
  
    FroudeN = MassFlux_tp**2 / (Gconst * D_int * rho_tp**2)
    WeberN = MassFlux_tp**2 * D_int *(SurfaceTension * rho_tp) 
    phi = (1-MassQual)**2 + MassQual**2 * (rho_l*f_go)/(rho_g*f_lo) + (3.24* MassQual**0.78 * (1-MassQual)**0.224 * (rho_l/rho_g)**0.91) / (FroudeN**0.045 * WeberN**0.035 * (DynVisc_g/DynVisc_l)**(-0.19) * (1 - DynVisc_g/DynVisc_l)**(-0.7))
        
    Array[TPM_name] = phi
       
    return Array[TPM_name]
