def Mishima_Hibiki_1996 (Array, Lockhart_Martinelli, D_int, liquid = True, TPM_name = 'phi^2_pred_Mishima_Hibiki_1996_l [-]'):
    '''Calculation of Mishima and Hibiki (1996) model for two phase flow multiplier - liquid or gas.
    Inputs are: Array - final table, Lockhart_Martinelli - L and M parameter X [-], D_int - internal diameter [m], liquid? - liquid/gas multiplier.'''    
    import numpy as np
    C = 21*(1-np.exp(-0.319*D_int*1e3))
    if liquid == True: #if is phi^2 liquid
      phi =  1 + C/Lockhart_Martinelli + 1/Lockhart_Martinelli**2
      Array[TPM_name] = phi
      return Array[TPM_name]
      
    else: #if is phi^2 gas
        phi =  1 + C*Lockhart_Martinelli + 1*Lockhart_Martinelli**2
        Array[TPM_name] = phi
        return Array[TPM_name]
