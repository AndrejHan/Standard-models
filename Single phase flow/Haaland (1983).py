def f_pred_Haaland (Array, Reynolds, Diameter_inter, FinHeight, limit, f_name = 'f_pred_Haaland [-]'):
    '''Calculation of predicted friction factor by Haaland correlation (by Fanning) for the microfined tubes.
    Inputs are: Array - final table, Reynolds - Reynolds number according to measured flow (liquid, gas, liquid-only, gas-only), Diameter_inter - internal diameter of the tube, FinHeight - height of the fin, limit - critical Re number.'''
    import pandas as pd
    import numpy as np
    
    Re_low =Reynolds[Reynolds < limit] #laminar flow
    f_low = 16./Re_low
    
    Re_high = Reynolds[Reynolds >= limit]  #turbulent flow
    f_high = 0.3086 / (np.log(6.9/Re_high + (FinHeight / (3.7 * Diameter_inter))**1.11 ))**2
     
    Array[f_name] = pd.concat([f_low,f_high])    
    return Array[f_name]   
  
