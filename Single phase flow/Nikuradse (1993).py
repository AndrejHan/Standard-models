def f_pred_Nikuradse (Array, Reynolds, limit, f_name = 'f_pred_Nikuradse [-]'):
    '''Calculation of predicted friction factor by Nikuradse correlation (by Fanning).
    Inputs are: Array - final table, Reynolds - Reynolds number according to measured flow (liquid, gas, liquid-only, gas-only), limit - critical Re number.'''
    import pandas as pd
    import numpy as np
    import scipy 
    from scipy import optimize
    
    Re_low =Reynolds[Reynolds < limit] #laminar flow
    f_low = 16./Re_low
    
    Re_high = Reynolds[Reynolds >= limit]  #turbulent flow
    def f_high_f(x):
        return (0.86*np.log(Re_high[i]*np.sqrt(x))-1/np.sqrt(x)-0.8)  
    for i in range (0,len(Re_high)):
        f_high =  scipy.optimize.fsolve(f_high_f,1e-3)
        Re_high[i] = f_high
    
    f_high = Re_high*0.25
               
    Array[f_name] = pd.concat([f_low,f_high])    
    return Array[f_name]   
    
