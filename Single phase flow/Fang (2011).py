def f_pred_Fang(Array, Reynolds, limit, f_name = 'f_pred_Fang [-]'):
    '''Calculation of predicted friction factor by Fang (2011) correlation (by Fanning) - smooth tube.
    Inputs are: Array - final table, Reynolds - Reynolds number according to measured flow (liqud, gas, liquid-only, gas-only) [-], limit - critical Re number [-].'''
    
    import numpy as np
    import pandas as pd
    
    Re_low = Reynolds[Reynolds < limit] #laminar flow
    f_low = 16./Re_low
    
    Re_high = Reynolds[Reynolds > limit]  #turbulent flow, usage of the Fang (2011)
    f_high = 0.25*0.25*(np.log10(150.39/(Re_high**0.98865) - 152.66/Re_high))**(-2)
     
    Array[f_name] = pd.concat([f_low,f_high])    
    return Array[f_name]
   
