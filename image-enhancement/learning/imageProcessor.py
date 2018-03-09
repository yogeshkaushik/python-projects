# -*- coding: utf-8 -*-
"""
    Image Enhancement
    ----------------------------------------------------------
    Current Implementation:
    - convert rgb to grey.
    - calculate mean threshold.
    - get binary image using the mean.

    Future Tasks:
    - check orientation and rotate accordingly.
    - select barcode region and crop it.
    ----------------------------------------------------------
    Requirements :

    Install and import ski-image
    ----------------------------------------------------------

    :author: Yogesh Kaushik <yogesh@revemarketing.com>.

"""
#import matplotlib.pyplot as plt //to plot images

import numpy as np
from skimage.feature import canny
from skimage import io
from skimage.filters import threshold_otsu, threshold_minimum, threshold_mean
from skimage.morphology import closing, opening

def enhance_image(url):
    img = io.imread(url,as_grey=True)
    threshold = threshold_mean(img)
    binaryImg = img > threshold
    afterOp = opening(binaryImg)
    return afterOp
