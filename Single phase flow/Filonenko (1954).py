def f_pred_Filonenko (Array, Reynolds, limit, f_name = 'f_pred_Filonenko [-]'):
    '''Calculation of predicted friction factor by Filonenko correlation (by Fanning) - smooth tube.
    Inputs are: Array - final table, Reynolds - Reynolds number according to measured flow (liquid, gas, liquid-only, gas-only) [-], limit - critical Re number [-].'''
    import pandas as pd
    import numpy as np
    
    Re_low =Reynolds[Reynolds < limit] #laminar flow
    f_low = 16./Re_low
    
    Re_high = Reynolds[Reynolds >= limit]  #turbulent flow
    f_high = 0.25*(0.79*np.log(Re_high)-1.64)**(-2)
     
    Array[f_name] = pd.concat([f_low,f_high])    
    return Array[f_name]  
