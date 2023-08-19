import numpy as np

def get_fourier(x):
    """
    Function that performs the Fourier calculation of a signal x and returns 
    its magnitude and frequency range.
    
    Parameters:
    x (numpy array): Signal to be transformed into Fourier domain.
    
    Returns:
    mag (numpy array): Magnitude of the signal's Fourier transform.
    freq (numpy array): Frequency domain of the signal's Fourier transform.
    """
    # Implemenet the FFT using NumPy, you can look for np.fft.fft
    # Remeber that the NumPy implementation of the FFT gives us the
    # two sided spectrum, therefore our frequency range should be
    # betwen 0 and 1. You can look for np.linspace for implementing 
    #the frequency range.
    ### BEGIN SOLUTION
    X = np.fft.fft(x)
    mag = np.absolute(X)
    
    samples = x.shape[0]
    freq = np.linspace(0,1, samples)
    return mag, freq
    ### END SOLUTION
    

def hamming_window(BW):
    """ 
    Function that calculates a Hamming window of a given transition bandwidth.
  
    Parameters: 
    BW (float): Transition bandwidth of the filter. The lenght of the filter is 
                given by M=4/BW.
                
    Returns: 
    numpy array: Returns Hamming window of a given M-kernel.
    """
    # Implement the Hamming Window
    ### BEGIN SOLUTION
    M = int(4/BW)
    x = np.arange(0,M,1)
    
    return 0.54 - 0.46*np.cos(2*np.pi*x/M)
    ### END SOLUTION

def blackman_window(BW):
    """ 
    Function that calculates a Blackman window of a given M-kernel.
  
    Parameters: 
    BW (float): Transition bandwidth of the filter. The lenght of the filter is 
                given by M=4/BW.
    Returns: 
    numpy array: Returns Blackman window of a given M-kernel.
    """
    # Implement the Blackman Window
    ### BEGIN SOLUTION
    M = int(4/BW)
    x = np.arange(0,M,1)
    
    return 0.42 - 0.5*np.cos(2*np.pi*x/M) + 0.08*np.cos(4*np.pi*x/M)
    ### END SOLUTION
    
    
def shifted_sinc_function(fc, BW):
    """ 
    Function that calculates a sinc shifted time response. The shifted sinc function has
    a shift value of M=4/BW.
  
    Parameters: 
    BW (float): Transition bandwidth of the filter. The lenght of the filter is 
                given by M=4/BW.
    fc (float): Cut-off frequency for the low-pass filter. Between 0 and 0.5.
  
    Returns: 
    numpy array: Returns sinc shifted time domain response.
    """
    # Remember that x is a value between 0 and M and your function returns
    # the shifted sinc calculation on every value of x.
    ### BEGIN SOLUTION
    M = int(4/BW)
    x = np.arange(0,M,1)
    shift = np.where(x == M/2)[0][0]
    h = np.zeros(M)
    
    h[:shift] = (np.sin(2*np.pi*(x[:shift]-M/2)*fc))/((x[:shift]-M/2)*np.pi)
    h[shift+1:] = (np.sin(2*np.pi*(x[shift+1:]-M/2)*fc))/((x[shift+1:]-M/2)*np.pi)
    h[shift] = 2*fc
    return h
    ### END SOLUTION
    
    
def spectral_reversal(h_lp):
    """
    Function that performs the spectral reversal of a low pass filter with
    coefficients h_lp and returns the high pass coefficients h_hp.
  
    Parameters: 
    h_lp (array): Array of numbers representing the low pass filter coefficients.
  
    Returns: 
    numpy array: Array of numbers representing the high pass filter coefficients.
    """
    ### BEGIN SOLUTION
    N = h_lp.shape[0]
    h_hp = h_lp * ((-1) ** np.arange(N))
    return h_hp
    ### END SOLUTION
    
    
def spectral_inversion(h_lp):
    """
    Function that performs the spectral inversion of a low pass filter with
    coefficients h_lp and returns the high pass coefficients h_hp.
  
    Parameters: 
    h_lp (array): Array of numbers representing the low pass filter coefficients.
  
    Returns: 
    numpy array: Array of numbers representing the high pass filter coefficients.
    """
    ### BEGIN SOLUTION
    h_hp = -h_lp
    center = int(len(h_hp)/2)
    h_hp[center] = h_hp[center] + 1
    return h_hp
    ### END SOLUTION
