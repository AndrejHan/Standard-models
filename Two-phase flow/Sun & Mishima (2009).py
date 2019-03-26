def Sun_Mishima_2009 (Array, Lockhart_Martinelli, Reynolds_l, Reynolds_g, D_int, rho_l, rho_g, SurfaceTension, MassQual, TPM_name = 'phi^2_pred_Sun_Mishima_2009_l [-]'):
    '''Calculation of Sun and Mishima (2009) model for two phase flow multiplier - liquid.
    Inputs are: Array - final table, Lockhart_Martinelli - L and M parameter X [-], Reynolds_l - Re number of liquid [-], Reynolds_g - Re number of gas [-], D_int - internal diameter [m], rho_l - density of liquid [kg/m^3], rho_g - density of gas [kg/m^3], SurfaceTension [N/m], MassQual - mass quality [-].'''    
    import numpy as np
    import pandas as pd
    La = (np.sqrt(SurfaceTension/(9.81*(rho_l - rho_g))))/D_int #Laplace constant
     
        #viscous flow
    visc = Reynolds_l[Reynolds_l<1000].index & Reynolds_g[Reynolds_g<2000].index
    C_v = 26*(1+Reynolds_l[visc]/1000)*(1 - np.exp(-0.153/(0.8+0.27*La[visc])))
    phi_v = 1 + C_v/Lockhart_Martinelli[visc]**1.19 + 1/Lockhart_Martinelli[visc]**2
    
        #turbulent flow:
    C_t = 1.79*(Reynolds_g.loc[~Reynolds_g.index.isin(visc)]/Reynolds_l.loc[~Reynolds_l.index.isin(visc)])**0.4 * ((1-MassQual.loc[~MassQual.index.isin(visc)])/MassQual.loc[~MassQual.index.isin(visc)])**(0.5)
    phi_t = 1 + C_t/Lockhart_Martinelli.loc[~Lockhart_Martinelli.index.isin(visc)]**1.19 + 1/Lockhart_Martinelli.loc[~Lockhart_Martinelli.index.isin(visc)]**2
    
    Array[TPM_name] = pd.concat([phi_v, phi_t])
    return Array[TPM_name]
