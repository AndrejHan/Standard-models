def Goto_2001 (Array, MassQual, MassFlux_tp, X, rho_g, Re_g, CrossSection, TPM_name = 'phi^2_pred_Haraguchi_1993_g [-]', HM_name = 'Dp/dz_pred_Goto_2001 [Pa/m]'):
    '''Calculation of Goto et al. (2001) model for two phase flow multiplier  - gas.
    Inputs are: Array - final table, MassQual - mass quality, MassFlux_tp - two phase mass flux, X - Lockhart and Martinelli parameter, rho_g - gas phase density, Re_g - Reynolds number of the gas phase, CrossSection - cross section of the tube.'''
    import pandas as pd
    import numpy as np
    De = np.sqrt((4*CrossSection)/np.pi)
        
    Re_1 = Re_g[Re_g <= 2000].index 
    f_1 = 16./Re_g[Re_1]
    
    Re_2 = Re_g[Re_g > 2000].index & Re_g[Re_g <= 2600].index
    f_2 =  0.000147 * Re_g[Re_2]**0.53
    
    Re_3 = Re_g[Re_g > 2600].index & Re_g[Re_g <= 6500].index
    f_3 =  0.046 * Re_g[Re_3]**(-0.2)
   
    Re_4 = Re_g[Re_g > 6500].index & Re_g[Re_g <= 12700].index
    f_4 =  0.00123 * Re_g[Re_4]**(0.21)
    
    Re_5 = Re_g[Re_g > 12700].index
    f_5 =  0.0092 * Re_g[Re_5]**0
           
    f = pd.concat([f_1,f_2,f_3,f_4,f_5])    
    
    phi = 1+ 1.64 * X**0.79
    
    Dp_dz = (2 * f * (MassFlux_tp*MassQual)**2)/(rho_g * De) * phi**2
    
    Array[TPM_name] = phi**2
    Array[HM_name]  = Dp_dz
    return Array[HM_name], Array[TPM_name]
