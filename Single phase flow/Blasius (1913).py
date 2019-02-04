def f_pred_Blasius (Array, Reynolds, limit, f_name = 'f_pred_Blasius [-]'):
    '''Calculation of predicted friction factor by Blasius(1913) correlation (by Fanning).
    Inputs are: Array - final table, Reynolds - Reynolds number according to measured flow (liquid, gas, liquid-only, gas-only), limit - critical Re number.'''
    import pandas as pd
    import numpy as np
    
    Re_low =Reynolds[Reynolds < limit] #laminar flow
    f_low = 16./Re_low
    
    Re_mid = Reynolds[(limit <= Reynolds) & (Reynolds < 20000)] #low turbulent flow
    f_mid = 0.079*Re_mid**-0.25

    Re_high = Reynolds[Reynolds >= 20000]  #high turbulent flow
    f_high = 0.046*Re_high**-0.2
     
    Array[f_name] = pd.concat([f_low,f_mid,f_high])    
    return Array[f_name] 
