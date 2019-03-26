def TPMultiplier_exp (Array, PressureGradient_tp, PressureGradient_sp, TPM_name = 'phi^2_exp [-]'):
    '''Calculation of Two-phase flow multipliers.
    Inputs are: Array - final table, PressureGradient_tp - two-phase experimentally obtaned, PressureGradient_sp - single phase -liquid/gas/liquid-only/gas-only.'''
    Array[TPM_name] = PressureGradient_tp/PressureGradient_sp
    return Array[TPM_name]
