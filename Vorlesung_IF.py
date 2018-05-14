def pv_annuität(C,i,N):
    '''
    Funktion zur Berechnung des Barwertes einer Annuität.
    
    Benötigter Input:
    
    C = jährliche Zahlungen
    
    i = Zinssatz
    
    N = Anzahl an Zahlungen
    
    Output:
    
    Barwert der Annuität berechnet nach:
    
    PV = C/i * (1 - 1/(1+i)**N)
    
    '''
    return C/i * (1 - 1/(1+i)**N)

def c_annuität(PV,i,N):
    return PV/(1/i * (1 - 1/(1+i)**N))