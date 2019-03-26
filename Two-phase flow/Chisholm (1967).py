def Chisholm_1967 (Array, Lockhart_Martinelli, Reynolds_l, Reynolds_g, liquid = True, TPM_name = 'phi^2_pred_Chisholm_1967_l [-]'):
    '''Calculation of Chisholm(1967) model for two phase flow multiplier - liquid or gas.
    Inputs are: Array - final table, Lockhart_Martinelli - L and M parameter X [-], Reynolds_l - Reynolds number of the liquid phase [-], Reynolds_g - Reynolds number of the gas phase [-], liquid? - liquid/gas multiplier.'''    
    import pandas as pd
    if liquid == True: #if is phi^2 liquid
        Re_vv = Reynolds_l[Reynolds_l<1000].index & Reynolds_g[Reynolds_g<2000].index 
        phi_vv = 1 + 5./Lockhart_Martinelli[Re_vv] + 1/Lockhart_Martinelli[Re_vv]**2
        
        Re_tv =  Reynolds_l[Reynolds_l>=1000].index & Reynolds_g[Reynolds_g<2000].index
        phi_tv = 1 + 10./Lockhart_Martinelli[Re_tv] + 1/Lockhart_Martinelli[Re_tv]**2
        
        Re_vt =  Reynolds_l[Reynolds_l<1000].index & Reynolds_g[Reynolds_g>=2000].index
        phi_vt = 1 + 12./Lockhart_Martinelli[Re_vt] + 1/Lockhart_Martinelli[Re_vt]**2
        
        Re_tt =  Reynolds_l[Reynolds_l>=1000].index & Reynolds_g[Reynolds_g>=2000].index
        phi_tt = 1 + 20./Lockhart_Martinelli[Re_tt] + 1/Lockhart_Martinelli[Re_tt]**2
        
        Array[TPM_name] = pd.concat([phi_vv, phi_tv, phi_vt, phi_tt])
        return Array[TPM_name] 
        
    else: #if is phi^2 gas
        Re_vv = Reynolds_l[Reynolds_l<1000].index & Reynolds_g[Reynolds_g<2000].index
        phi_vv = 1 + 5*Lockhart_Martinelli[Re_vv] + 1*Lockhart_Martinelli[Re_vv]**2
        
        Re_tv =  Reynolds_l[Reynolds_l>=1000].index & Reynolds_g[Reynolds_g<2000].index
        phi_tv = 1 + 10*Lockhart_Martinelli[Re_tv] + 1*Lockhart_Martinelli[Re_tv]**2
    
        Re_vt =  Reynolds_l[Reynolds_l<1000].index & Reynolds_g[Reynolds_g>=2000].index
        phi_vt = 1 + 12*Lockhart_Martinelli[Re_vt] + 1*Lockhart_Martinelli[Re_vt]**2
        
        Re_tt =  Reynolds_l[Reynolds_l>=1000].index & Reynolds_g[Reynolds_g>=2000].index
        phi_tt = 1 + 20*Lockhart_Martinelli[Re_tt] + 1*Lockhart_Martinelli[Re_tt]**2
        
        Array[TPM_name] = pd.concat([phi_vv, phi_tv, phi_vt, phi_tt])
        return Array[TPM_name]
