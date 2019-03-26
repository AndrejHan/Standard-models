def Shannak_2008 (Array, MassQual, DynVisc_l, DynVisc_g, MassFlux_tp, D_int, rho_l, rho_g, rho_tp, FinHeight,  HM_name = 'Dp/dz_pred_Shannak_2008_tp [Pa/m]'):
    '''Calculation of Shannak et al. (2008) model for the two phase friction factor of the rough tubes.
    Inputs are: Array - final table, MassQual - mass quality [-], DynVisc_l - Dynamic viscosity of liquid [Pa*s], DynVisc_g - Dynamic viscosity of gas [Pa*s], MassFlux_tp - two phase mass flux [kg/m^2/s], D_int - internal diameter [m], rho_l - liquid phase flow density [kg/m^3], rho_g - liquid phase flow density [kg/m^3], rho_tp - two-phase flow density [kg/m^3], FinHeight - height of the fin [m].'''
    import pandas as pd
    import numpy as np
    Re_tp = ((MassFlux_tp * D_int) * (MassQual**2 + (1-MassQual)**2 * (rho_g/rho_l))) / (DynVisc_g*MassQual + DynVisc_l*(1-MassQual) *  (rho_g/rho_l))
    
    Re_low = Re_tp[Re_tp < 2000] #laminar flow
    f_low = 16./Re_low
    
    Re_high = Re_tp[Re_tp >= 2000]  #turbulent flow
    f_high = 0.25 * (-2*np.log10(1./3.7065 * FinHeight/D_int - 5.0452/Re_high * np.log10(1./2.8257 * (FinHeight/D_int)**1.1098 + 5.8506/Re_high**0.8981)))**(-2) 
    f = pd.concat([f_low,f_high])    
    
    Dp_dz = (2 * f * MassFlux_tp**2)/(rho_tp * D_int)
    Array[HM_name]  = Dp_dz
    return Array[HM_name]
