# Image Compression with Fast Fourier Transform (FFT)
Coursework from Fourier Analysis II class by Prof. James Cannon at Kyushu University

(See full report: [Fourier Course work Komsun Tamana.pdf](https://github.com/komxun/Image-Compression-with-FFT/files/11452754/Fourier.Course.work.Komsun.Tamana.pdf))


# 1. Introduction
Fast Fourier Transform (FFT) has been known in an application for one-dimensional signals processing such as noise filtering. 
This concept can also be generalized to a higher spatial dimension including two-dimensional signals and an image’s pixels matrix. 
In this work, the applications of Fast Fourier Transform for image compression has been investigated with examples in Python. 

# 2. Principles
## 2.1 2D-Fourier Transform
The two-dimensional Fourier transform of a matrix of data  $X \in \mathbb{R}^{n \times m}$ is achieved by first applying the one-dimensional Fourier transform to every row of the matrix, 
and then applying the one-dimensional Fourier transform to every column of the intermediate matrix. 
Switching the order of taking the Fourier transform of rows and columns does not change the result.

|![image](https://github.com/komxun/Image-Compression-with-FFT/assets/133139057/e66445b3-912c-47e0-aed4-864c05b660c3)|
|:--:| 
| *Schematic of 2D FFT (Brunton & Kutz, 2017, p.89)* |

## 2.2 Fast Fourier Transform (FFT)
Unlike light and sound wave, digital images are discrete since the pixels are not continuous. 
Thus, Discrete Fourier Transform (DFT) should be applied instead of Fourier Transform. However, DFT process often takes long time and not practical. 
Hence, the Fast Fourier Transform (FFT) is more suitable for digital image processing applications.

# 3. Digital Image Compression with 2D FFT
When a digital image, says 1 Mega pixel’s image, is Fourier transformed, there will be a million Fourier coefficients. 
However, it is observed that most these Fourier coefficients of the images are neglectably small. 
It is only a few large Fourier coefficients that keep the important information and quality of the images. 
Therefore, we can threshold and filter out those insignificant Fourier coefficients and keep only a small amount of the largest Fourier coefficients, 
then inverse Fourier transform back to get the compressed image. As a result, the file size of digital image could be reduced without lowering any noticeable image’s quality.
|![image](https://github.com/komxun/Image-Compression-with-FFT/assets/133139057/2a5a4e79-13b9-475e-a679-90a1631c7974)|
|:--:| 
| *Schematic of image compression processing using FFT* |

In this work, 2D FFT will be executed using **np.fft.fft2 **, then items in 2D FFT vector will be sorted by magnitude. The obtained Fourier coefficients will be kept only for the largest 10%, 5%, 1%, and 0.2% for compression performance comparison.
https://github.com/komxun/Image-Compression-with-FFT/blob/76eecd5e95dd2358cc659fd4c35b44e7e382147b/main_img_compress.py#L17C6-L26

# 4. Results
The image compression is done with various thresholds keeping 10%, 5%, and 0.2% of the largest Fourier coefficients. Here the image is converted to grayscale for simplicity.
|![image](https://github.com/komxun/Image-Compression-with-FFT/assets/133139057/673fb463-213e-4c6b-a730-1af1f637ed57)|
|:--:| 
| *Image compression using 2D FFT examples: (a) original image in gray scale,  compressed image keeping (b) 10% (c) 5% (d) 0.2% of the largest Fourier coefficients* |

# 5. Discussion
As shown in the figure, the result from keeping 5% and 10% of the largest Fourier coefficients gave a good overall image quality. 
On the other hand, by keeping 0.2% of the largest Fourier coefficients, the degradation of the compressed image can be visibly seen. 
The original image’s file size is 5567 KB. The compressed images’ file size by keeping 10%, 5%, and 0.2% of the largest Fourier coefficients are 5266 KB, 4824 KB, and 3077 KB respectively.

# 6. Conclusion
The method of image compression using FFT can also be applied to any two-dimensional signals such as a digital audio. There are more techniques of image compression such as an image compression and denoising using 2D wavelet transform.

# References
[1] Steven L. Brunton., & J. Nathan Kutz. (2017). _Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control_. New York, U.S.: Cambridge University Press.

[2] Chen, C. (2020). _Digital Image Processing using Fourier Transform in Python_. Retrieved 
29 January 2021, from https://hicraigchen.medium.com/digital-image-processing-using-fourier-transform-in-python-bcb49424fd82

[3] Pysource. (2018, August 4). _Fourier Transform – OpenCV 3.4 with python 3 Tutorial 35_ [Video]. Youtube. https://www.youtube.com/watch?v=cLHAUhGkzwQ&list=RDCMUC5hHNks012Ca2o_MPLRUuJw&start_radio=1&ab_channel=Pysource




