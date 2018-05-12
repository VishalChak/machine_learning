#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:08:44 2017

@author: vishal
"""

import numpy as np
import numpy.random as rnd

X = 2 * rnd.rand(100, 1)
y = 4 + 3 * X + rnd.randn(100, 1)


import numpy.linalg as LA