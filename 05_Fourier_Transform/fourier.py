import numpy as np

def dft(x):
    """ 
    Function that calculates the DFT of an input signal x.
  
    Parameters: 
    x (numpy array): Array of numbers representing the input signal to be transformed.
  
    Returns: 
    rex (numpy array): Real DFT part of input signal x
    imx (numpy array): Imaginary DFT part of input signal x
  
    """
    
    N = len(x)
    M = int(N/2) + 1
    rex = np.zeros((M,1))
    imx = np.zeros((M,1))
    
    ### BEGIN SOLUTION

    for k in range(M):
        for i in range(N):
            rex[k][0] = rex[k][0] + x[i][0]*np.cos(2*np.pi*k*i/N)
            imx[k][0] = imx[k][0] - x[i][0]*np.sin(2*np.pi*k*i/N)
    ### END SOLUTION        
    
    return rex, imx   


def dft_magnitude(rex, imx):
    """ 
    Function that calculates the magnitude of an real and imaginary signal x.
  
    Parameters: 
    rex (numpy array): Array of numbers representing the real part of the DFT signal.
    imx (numpy array): Array of numbers representing the imaginary part of the DFT signal.
  
    Returns: 
    numpy array: Returns magnitude of the real and imaginary signal.
  
    """
    ### BEGIN SOLUTION
    return np.sqrt(rex**2 + imx**2)
    ### END SOLUTION
    
    
    
def arctan_correct(rex, imx, phase):
    """ 
    Function that corrects the arctan calculation. If both the real and 
    imaginary parts are negative, subtract 180 (or 𝜋 radians) from the
    calculated phase. If the real part is negative and the imaginary part
    is positive, add 180 (or 𝜋 radians)
  
    Parameters: 
    rex (numpy array): Array of numbers representing the real part of the DFT signal.
    imx (numpy array): Array of numbers representing the imaginary part of the DFT signal.
    phase (numpy array): Array of numbers representing the phase of the DFT signal.
  
    Returns: 
    numpy array: Returns corrected arctan calculation of phase.
  
    """
    
    N = rex.shape[0]
    output = np.copy(phase)
    
    ### BEGIN SOLUTION

    for i in range(N):
        if rex[i][0]<0:
            if imx[i][0]<0:
                output[i]=phase[i] - np.pi
                #print('minus pi correction')
            elif imx[i][0]>0:
                output[i]=phase[i] + np.pi
                #print('plus pi correction')
                
    ### END SOLUTION
    return output



def unwrap(phase):
    """ 
    Function that ensures that all appropriate multiples of 2𝜋 have been included.
  
    Parameters: 
    phase (numpy array): Array of numbers representing the phase of the DFT signal.
  
    Returns: 
    numpy array: Returns unwrapped phase.
  
    """
    
    N = phase.shape[0]
    uwphase = np.zeros(phase.shape)
    
    ### BEGIN SOLUTION    
    for i in range(N):
        c = np.round((uwphase[i-1][0]-phase[i][0])/(2*np.pi))#.astype('int')
        uwphase[i] = phase[i] + c*2*np.pi
    
    ### END SOLUTION
    return uwphase



def dft_phase(rex, imx, correct_arctan=True, correct_unwrap=True):
    """ 
    Function that calculates the phase of an real and imaginary signal x. 
    Solving the different drawbacks that might occur.
  
    Parameters: 
    rex (numpy array): Array of numbers representing the real part of the DFT signal.
    imx (numpy array): Array of numbers representing the imaginary part of the DFT signal.
    correct_arctan (boolean): If True arctan correction is performed.
    correct_unwrap (boolean): If True phase abiguity correction is performed.
  
    Returns: 
    numpy array: Returns phase of the real and imaginary signal.
  
    """
    N = rex.shape[0]
    
    #SOLVE Drawback 2: Divide by zero error
    ### BEGIN SOLUTION  
    rex[rex==0] = 1e-18
    phase = np.arctan(imx/rex)
    ### END SOLUTION
    
    #SOLVE Drawback 3: Incorrect arctan
    ### BEGIN SOLUTION  
    if correct_arctan==True:
        phase_correct = arctan_correct(rex, imx, phase)
    else:
        phase_correct = phase
    ### END SOLUTION
                    
    #SOLVE Drawback 5: 2𝜋 ambiguity of the phase 
    ### BEGIN SOLUTION  
    if correct_unwrap==True:
        uwphase = unwrap(phase_correct)
    else:
        uwphase = phase_correct
    ### END SOLUTION
    
    return uwphase


def frequency_domain(x, style='fraction', **kwargs):
    """ 
    Function that calculates the frequency domain independent variable.

    Parameters: 
    x (numpy array): Array of numbers representing the input signal inthe Fourier domain
    to  obtain the frequency independent variable.
    style (string): String value that selects between frequency domain's 
    independent variable.
        'samples' returns number of samples between 0 to N/2
        'fraction' returns a fraction of the sampling rate between 0 to 0.5
        'natural' returns the natural frequency between 0 and pi.
        'analog' returns analog frequency between 0 and fsamp/2
    fsamp (float): Float value representing the sampling frequency. 
        (Only used for 'analog' style).

    Returns: 
    numpy array: Returns frequency domain's independent variable.

        """
    N = x.shape[0]
    t = np.arange(N)
    
    ### BEGIN SOLUTION
       
    if(style=='fraction'):
        return t/(2*(N-1))
    elif(style=='natural'):
        return np.pi*(t/(2*(N-1)))
    elif(style=='analog'):
        return kwargs['fsamp']*(t/(2*(N-1)))
    elif(style=='samples'):
        return t
    else:
        return t
    
    ### END SOLUTION
