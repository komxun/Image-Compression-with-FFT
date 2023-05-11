from matplotlib.image import imread 
from matplotlib.pyplot import imsave
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [5, 5]
plt.rcParams.update({'font.size': 18})

A = imread('artemis_i_mission_map_nov_2020.jpg')
B = np.mean(A, -1);               # convert RGB to gray scale for simplicity
plt.figure()
plt.imshow(B, cmap='gray')
plt.title('Original image in gray scale')

plt.axis('off')

Bt = np.fft.fft2(B)
Btsort = np.sort(np.abs(Bt.reshape(-1)))   # sort by magnitude

#zero out all small coefficients and inverse transform

for keep in (0.1, 0.05, 0.01, 0.002): # keep the largest 10%, 5%, 1%, 0.2% of Fourier coefficients
    thresh = Btsort[int(np.floor((1-keep)*len(Btsort)))]  # create the sorted-values vector
    indices = np.abs(Bt)>thresh             # Find small indices
    Bt_low = Bt*indices                     # Threshold small indices
    B_comp = np.fft.ifft2(Bt_low).real      # Compressed image
    imsave(('Compressed_' + str(keep*100) + '_percent.jpg'), B_comp, cmap = 'gray')
    #imsave(('new_NASA_Compressed_'+str(keep*100)+'_percent.jpg'), B_comp, cmap='gray' )
    plt.figure()
    plt.imshow(B_comp, cmap='gray')
    plt.axis('off')
    plt.title('new_Compressed image: keep = '+str(keep*100)+'%')
    