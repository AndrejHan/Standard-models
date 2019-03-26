def Awad_Muzychka_2008(Array, MassQual, DynVisc_l, DynVisc_g, MassFlux_tp, D_int, rho_tp,  HM_name = 'Dp/dz_pred_Awad_Muzychka_2008_tp [Pa/m]'):
    '''Calculation of Awad and Muzychka (2008) (definition 4) model for two phase dynamic viscosity. For the calculation of friction factor is used Fang(2011) correlation (by Fanning).
    Inputs are: Array - final table, MassQual - mass quality [-], DynVisc_l - Dynamic viscosity of liquid [Pa*s], DynVisc_g - Dynamic viscosity of gas [Pa*s], MassFlux_tp - two phase mass flux [kg/m^2/s], D_int - internal diameter [m], rho_tp - two phase flow density [kg/m^3].'''
    import pandas as pd
    import numpy as np
    mu_tp = DynVisc_g*(2*DynVisc_g + DynVisc_l - 2*(DynVisc_g - DynVisc_l)*(1-MassQual))/(2*DynVisc_g + DynVisc_l + (DynVisc_g - DynVisc_l)*(1-MassQual))
    Re_tp = (MassFlux_tp * D_int)/mu_tp
        
    Re_low = Re_tp[Re_tp < 2000] #laminar flow
    f_low = 16./Re_low
    Re_high = Re_tp[Re_tp >= 2000]  #turbulent flow
    f_high = 0.25*0.25*(np.log10(150.39/(Re_high**0.98865) - 152.66/Re_high))**(-2) 
    f = pd.concat([f_low,f_high])    
    
    Dp_dz = (2 * f * MassFlux_tp**2)/(rho_tp * D_int)
    Array[HM_name]  = Dp_dz
    return Array[HM_name]
