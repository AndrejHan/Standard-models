def f_pred_JensenVlakancic (Array, f_pred_smooth, Reynolds, CrossSection_smooth, CrossSection_microfin, FinHelixAngle, FinHeight, Diameter_inter_microfin, FinNumber, FinPitch, limit, f_name = 'f_pred_JensenVlakancic [-]'):
    '''Calculation of predicted friction factor by Jensen and Vlakancic correlation (by Fanning) for the microfined tubes.
    Inputs are: Array - final table, f_pred_smooth - friction factor predicted for the smooth tube [-], Reynolds - Reynolds number according to measured flow (l, g, lo, go) [-], CrossSection_smooth - Cross section of the pipe as smooth [m^2], CrossSection_microfin - Cross section of the pipe with fins [m^2], FinHelixAngle - Helix angle of fins [m], FinHeight - Height of the fin [m], limit - critical Re number [-].'''
    import pandas as pd
    import numpy as np    
   
    Re_low = Reynolds[Reynolds < limit].index #laminar flow
    f_low = f_pred_smooth[Re_low]
   
    Re_high = Reynolds[Reynolds >= limit].index  #turbulent flow

    if (2*FinHeight/Diameter_inter_microfin) <= 0.04: # non dimensional fin height
        a = 1.577
        b = 0.64
        c = 0.53
        d = 0.28
        
        MeanFinThickness = FinPitch / np.cos(np.deg2rad((FinHelixAngle)) - np.pi/4*(Diameter_inter_microfin**2 - Diameter_inter_equivalent**2)/(FinNumber*FinHeight) # mean fin thickness
        lc_D = 1 - a*( FinNumber *np.sin (np.deg2rad(FinHelixAngle))/np.pi)**b * (2*FinHeight/Diameter_inter_microfin)**c * ((np.pi/FinNumber - MeanFinThickness/Diameter_inter_microfin) * np.cos (np.deg2rad(FinHelixAngle)))** d
        f_high = f_pred_smooth[Re_high]*( (lc_D)**-1.25 * (CrossSection_smooth/CrossSection_microfin)**1.75 - (0.0151/ f_pred_smooth[Re_high])* ((lc_D)**-1.25 * (CrossSection_smooth/CrossSection_microfin)**1.75 - 1) * np.exp(-Reynolds[Re_high]/6780))
        Array[f_name] = pd.concat([f_low,f_high])    
        return Array[f_name]
        
        
    elif ((2*FinHeight/Diameter_inter_microfin) > 0.04) & ((2*FinHeight/Diameter_inter_microfin) <= 0.06): # non dimensional fin height (high fin and micro fin transient group)
        a = 0.994
        b = 0.89
        c = 0.44
        d = 0.41
        
        MeanFinThickness = FinPitch / np.cos(np.deg2rad(FinHelixAngle)) - np.pi/4*(Diameter_inter_microfin**2 - Diameter_inter_equivalent**2)/(FinNumber*FinHeight) # mean fin thickness
        lc_D = 1 - a*( FinNumber *np.sin (np.deg2rad(FinHelixAngle))/np.pi)**b * (2*FinHeight/Diameter_inter_microfin)**c * ((np.pi/FinNumber - MeanFinThickness/Diameter_inter_microfin) * np.cos (np.deg2rad(FinHelixAngle)))** d
        f_high = f_pred_smooth[Re_high]*( (lc_D)**-1.25 * (CrossSection_smooth/CrossSection_microfin)**1.75 - (0.0151/ f_pred_smooth[Re_high])* ((lc_D)**-1.25 * (CrossSection_smooth/CrossSection_microfin)**1.75 - 1) * np.exp(-Reynolds[Re_high]/6780))
        
        Array[f_name] = pd.concat([f_low,f_high])    
        return Array[f_name]
