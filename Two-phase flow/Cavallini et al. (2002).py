def Cavallini_2002 (Array, rho_l, rho_g, DynVisc_l, DynVisc_g, f_lo, f_go, MassQual, MassFlux_tp, D_int, SurfaceTension,TPM_name = 'phi^2_pred_Cavallini_2002_lo [-]'):
    '''Calculation of Cavallini et al. (2002) model for two phase flow multiplier - liquid only.
    Inputs are: Array - final table, rho_l - Density of the liquid phase [kg/m^3], rho_g - Density of the gas phase [kg/m^3], DynVisc_l - Dynamic viscosity of the liquid [Pa*s], DynVisc_g - Dynamic viscosity of the gas [Pa*s], MassQual - mass quality [-], MassFlux_tp - Total mass flux [kg/m^2/s], D_int - internal diameter of the tube [m], SurfaceTension - surface tension of the fluid [N/m].'''    
  
    phi = (1-MassQual)**2 + MassQual**2 * (rho_l*f_go)/(rho_g*f_lo) + (1.262 * MassQual**0.6978 * (rho_l/rho_g)**0.3278 * (DynVisc_g/DynVisc_l)**(-1.181) * (1 - DynVisc_g/DynVisc_l)**(3.477) * rho_g*SurfaceTension) / (MassFlux_tp**2 * D_int)
        
    Array[TPM_name] = phi
       
    return Array[TPM_name]
