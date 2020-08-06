# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
from skimage import io
from skimage import transform as tf
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:/Desktop/illegal stuff/Tesseract/tesseract.exe'
def get_image():
    heroes_together = cv2.imread('D:/Desktop/illegal stuff/example_image_for_illegal_stuff.png')
    split_heroes(heroes_together)
    
def split_heroes(heroes_together):
    for i in range(2):
        individual_hero = heroes_together[0:155,115+150*i:235+150*i,:]
        identify_hero(individual_hero)
    for i in range(3):
        individual_hero = heroes_together[155:310,45+150*i:155+150*i,:]
        identify_hero(individual_hero)
    
    
def identify_hero(individual_hero):
    individual_hero_portrait = individual_hero[0:90,:,:]
    individual_hero_power = individual_hero[85:135,:,:]
    print(np.max(individual_hero_power),np.min(individual_hero_power))
    print(type(individual_hero_power))
    # Create Afine transform
    afine_tf = tf.AffineTransform(shear=0.25)
    
    # Apply transform to image data
    individual_hero_power = tf.warp(individual_hero_power, inverse_map=afine_tf)
    print(np.max(individual_hero_power),np.min(individual_hero_power))

    print(type(individual_hero_power))
    individual_hero_stars = individual_hero[130:155,:,:]
    cv2.imshow('image', individual_hero_portrait)
    cv2.waitKey(0)
    cv2.imshow('image', individual_hero_power)
    cv2.waitKey(0)
    print(pytesseract.image_to_string(individual_hero_power))
    cv2.imshow('image', individual_hero_stars)
    cv2.waitKey(0)
    
get_image()