def Chisholm_1973(Array, Chisholm_Y, MassQual, MassFlux_tp, TPM_name = 'phi^2_pred_Chisholm_1973_lo [-]'):
    '''Calculation of Chisholm (1973) model for two phase flow multiplier - liquid.
    Inputs are: Array - final table, MassQual - mass quality, MassFlux_tp - two phase mass flux.'''    
    import numpy as np
    import pandas as pd
    
    case1 = Chisholm_Y[0 < Chisholm_Y].index & Chisholm_Y[Chisholm_Y < 9.5].index & MassFlux_tp[MassFlux_tp >= 1900].index
    B1 = 55/np.sqrt(MassFlux_tp[case1])
    phi1 = 1 + (Chisholm_Y[case1]**2 - 1)*(B1 * (MassQual[case1] * (1- MassQual[case1]))**0.875 + MassQual[case1]**1.75)
    
    case2 = Chisholm_Y[0 < Chisholm_Y].index & Chisholm_Y[Chisholm_Y < 9.5].index & MassFlux_tp[MassFlux_tp < 1900].index & MassFlux_tp[MassFlux_tp > 500].index
    B2 = 2400
    phi2 = 1 + (Chisholm_Y[case2]**2 - 1)*(B2 * (MassQual[case2] * (1- MassQual[case2]))**0.875 + MassQual[case2]**1.75)
    
    case3 = Chisholm_Y[0 < Chisholm_Y].index & Chisholm_Y[Chisholm_Y < 9.5].index & MassFlux_tp[MassFlux_tp <= 500].index
    B3 = 4.8
    phi3 = 1 + (Chisholm_Y[case3]**2 - 1)*(B3 * (MassQual[case3] * (1- MassQual[case3]))**0.875 + MassQual[case3]**1.75)
    
    case4 = Chisholm_Y[9.5 <= Chisholm_Y].index & Chisholm_Y[Chisholm_Y < 28].index & MassFlux_tp[MassFlux_tp <= 600].index
    B4 = 520/(Chisholm_Y[case4] * np.sqrt(MassFlux_tp[case4]))
    phi4 = 1 + (Chisholm_Y[case4]**2 - 1)*(B4 * (MassQual[case4] * (1- MassQual[case4]))**0.875 + MassQual[case4]**1.75)
    
    case5 = Chisholm_Y[9.5 <= Chisholm_Y].index & Chisholm_Y[Chisholm_Y < 28].index & MassFlux_tp[MassFlux_tp > 600].index
    B5 = 21/Chisholm_Y[case5]
    phi5 = 1 + (Chisholm_Y[case5]**2 - 1)*(B5 * (MassQual[case5] * (1- MassQual[case5]))**0.875 + MassQual[case5]**1.75)
    
    case6 = Chisholm_Y[Chisholm_Y >= 28].index
    B6 = 15000/(Chisholm_Y[case6]**2 * np.sqrt(MassFlux_tp[case6]))
    phi6 = 1 + (Chisholm_Y[case6]**2 - 1)*(B6 * (MassQual[case6] * (1- MassQual[case6]))**0.875 + MassQual[case6]**1.75)
    
    Array[TPM_name] = pd.concat([phi1, phi2, phi3, phi4, phi5, phi6])
    return Array[TPM_name]
