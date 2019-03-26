def Zhang_2010 (Array, Lockhart_Martinelli, D_int, rho_l, rho_g, SurfaceTension, flow = 'adiabatic gas-liquid', liquid = True, TPM_name = 'phi^2_pred_Zhang_2010_l [-]'):
    '''Calculation of Zhang et al. (2010) model for two phase flow multiplier - liquid or gas.
    Inputs are: Array - final table, Lockhart_Martinelli - L and M parameter X, D_int - internal diameter, rho_l - density of liquid, rho_g - density of gas, SurfaceTension, flow = 'adiabatic gas-liquid'/'adiabatic vapor-liquid'/'flow boiling', liquid? - liquid/gas multiplier.'''    
    import numpy as np
    La = (np.sqrt(SurfaceTension/(9.81*(rho_l - rho_g))))/D_int #Laplace constant
    
    if liquid == True: #if is phi^2 liquid
        if flow == 'adiabatic gas-liquid':
            C = 21*(1-np.exp(-0.674/La))
            phi =  1 + C/Lockhart_Martinelli + 1/Lockhart_Martinelli**2
            Array[TPM_name] = phi
            return Array[TPM_name]
      
        elif flow == 'adiabatic vapor-liquid':
            C = 21*(1-np.exp(-0.142/La))
            phi =  1 + C/Lockhart_Martinelli + 1/Lockhart_Martinelli**2
            Array[TPM_name] = phi
            return Array[TPM_name]
          
        else: #flow boiling
            C = 21*(1-np.exp(-0.674/La))
            phi =  1 + C/Lockhart_Martinelli + 1/Lockhart_Martinelli**2
            Array[TPM_name] = phi
            return Array[TPM_name]
            
    else: #if is phi^2 gas
        if flow == 'adiabatic gas-liquid':
            C = 21*(1-np.exp(-0.674/La))
            phi =  1 + C*Lockhart_Martinelli + 1*Lockhart_Martinelli**2
            Array[TPM_name] = phi
            return Array[TPM_name]
      
        elif flow == 'adiabatic vapor-liquid':
            C = 21*(1-np.exp(-0.142/La))
            phi =  1 + C*Lockhart_Martinelli + 1*Lockhart_Martinelli**2
            Array[TPM_name] = phi
            return Array[TPM_name]
          
        else: #flow boiling
            C = 21*(1-np.exp(-0.674/La))
            phi =  1 + C*Lockhart_Martinelli + 1*Lockhart_Martinelli**2
            Array[TPM_name] = phi
            return Array[TPM_name]
