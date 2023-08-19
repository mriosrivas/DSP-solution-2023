import numpy as np
import matplotlib.pyplot as plt
import scipy.signal



def filter_frequency_response(c, d, w = np.arange(0, np.pi, 0.1)):
    """ 
    Function that generates the frequency response of a digital filter given the coeficients of 
    polynomials c0 + c_1*x + c_2*x^2 + ... and d0 + d_1*x + d_2*x^2 + ...
    This function evaluates the transfer function 
    H(x)=(c0 + c_1*x + c_2*x^2 + ...)/(d0 + d_1*x + d_2*x^2 + ...) where x is an element in vector w.
  
    Parameters: 
    w (numpy array): Array of natural frequency values.
    c (numpy array): Array of recursion coefficients c.
    d (numpy array): Array of recursion coefficients d.
  
    Returns: 
    numpy array: Returns filter response.
  
    """
    ### BEGIN SOLUTION
    z = np.exp(1j*w)
    
    c_degree = np.arange(0,len(c))
    d_degree = np.arange(0,len(d))
    
    N = len(z)
    nc = len(c_degree)
    nd = len(d_degree)
    
    ZC = (np.repeat(z,nc, axis = 0)).reshape(N,nc)
    ZD = (np.repeat(z,nd, axis = 0)).reshape(N,nd)
    
    z_c = np.dot((ZC**c_degree),c)
    z_d = np.dot((ZD**d_degree),d)
    return z_c/z_d
    ### END SOLUTION
    
    
def zeros_poles_gain(c, d):
    """ 
    Function that calculates the zeros, poles and gain of a given transfer function which consists of
    the coeficients of polynomials c0 + c_1*x + c_2*x^2 + ... and d0 + d_1*x + d_2*x^2 + ...
  
    Parameters: 
    c (numpy array): Array of recursion coefficients c.
    d (numpy array): Array of recursion coefficients d.
  
    Returns: z,p,g
    z (numpy array): Zeros of transfer function.
    p (numpy array): Poles of transfer function.
    g (numpy array): Gain of transfer function.
  
    """
    ### BEGIN SOLUTION
    return scipy.signal.tf2zpk(np.flip(c),np.flip(d))
    ### END SOLUTION
