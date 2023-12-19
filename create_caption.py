#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   create_celeba_caption_v4.py
@Time    :   2023/03/24 20:46:59
@Author  :   Weihao Xia (xiawh3@outlook.com)
@Version :   4.0
@Desc    :   This script can generate image captions given attribute annotations. 
             Please notice that the text part of the released multi-modal-celeba-hq dataset is not based on this scripts.
             This version of the script uses a pcfg-like idea and offers improved readability and extensibility compared to the original.
             You can alternatively use cntk.pcfg package for sentence generation.
'''
import os
import pandas as pd
from random import randint, choice, shuffle, sample

ALL_ATTRIBUTE =  False # True 
NUM_CAPTION = 10 if ALL_ATTRIBUTE is False else 1

# Create a dictionary with attributes and their values
ATTRIBUTES = {
    'IsAttributes': ['Attractive', 'Bald', 'Chubby', 'Young', 'Smiling'],
    'HasAttributes': ['Eyeglasses', 'Arched_Eyebrows', 'Bags_Under_Eyes', 'Bangs', 'Big_Lips', 'Big_Nose', 'Black_Hair',
               'Blond_Hair', 'Brown_Hair', 'Bushy_Eyebrows', 'Double_Chin', 'Goatee', 'Gray_Hair', 'Straight_Hair',
               'Sideburns', 'Rosy_Cheeks', 'Receding_Hairline', 'Pointy_Nose', 'Pale_Skin', 'Oval_Face', 'Narrow_Eyes',
               'Mustache', 'Mouth_Slightly_Open', 'High_Cheekbones', 'Wavy_Hair'],
    'WearAttributes': ['Wearing_Necktie', 'Wearing_Necklace', 'Wearing_Lipstick', 'Wearing_Hat', 'Wearing_Earrings',
                'Heavy_Makeup'],
}

gender = {
    'female': ['She', 'This woman', 'The woman', 'The person', 'This person'], # in the picture, in the image, the entire face of 
    'male': ['He', 'This man', 'The man', 'The person', 'This person']
}

IsVerb = [' is ', ' looks ', ' appears to be ']
WearVerb =[' wears ', ' is wearing '] 
HaveVerb = [' has ', ' is with ']

def get_subject(img_attribute):
    '''
    This function gives options of subject for a given image.
    '''
    if img_attribute['Male'] == str(-1):
        return gender['female']
    else:
        return gender['male']
        
def get_feature(img_attribute):
    '''
    This function gives three categories attributes for a given image. The output for image 29999.jpg is shown below.
    feature = {'IsAttributes': ['Attractive', 'Smiling'], 
    'HasAttributes': ['Bangs', 'Brown_Hair', 'Rosy_Cheeks', 'Mouth_Slightly_Open', 'High_Cheekbones', 'Wavy_Hair'], 
    'WearAttributes': ['Wearing_Lipstick', 'Wearing_Earrings', 'Heavy_Makeup']}
    '''
    feature = {}
    for attribute, values in ATTRIBUTES.items():
        feature[attribute] = [value for value in values if img_attribute[value] == str(1)]
    return feature

def get_caption(img_attribute, num_caption):
    '''
    This function gives a certain numbers of captions for every images in the dataset.
    '''
    subject = get_subject(img_attribute)
    feature = get_feature(img_attribute)

    captions = []

    # randomly select number of captions to generate
    for _ in range(num_caption):

        if ALL_ATTRIBUTE:
            IsAttributes = ', '.join(feature['IsAttributes']).lower()[::]
            HasAttributes = ', '.join(feature['HasAttributes']).replace('_', ' ').lower()[::]
            WearAttributes = ', '.join(feature['WearAttributes']).replace('Wearing_', '').replace('_', ' ').lower()[::]

            caption = f'The person in the picture is {IsAttributes}. {choice(subject)}{choice(HaveVerb)}{HasAttributes}. {choice(subject)}{choice(WearVerb)}{WearAttributes}.'
            captions.append(caption)

        else:
            # get number of attributes in each category
            len_i = len(feature['IsAttributes'])
            len_h = len(feature['HasAttributes'])
            len_w = len(feature['WearAttributes'])

            # randomly select number of attributes to use for each category
            c_i = randint(1, len_i)  if len_i > 1 else len_i
            c_h = randint(1, len_h)  if len_h > 1 else len_h
            c_w = randint(1, len_w)  if len_w > 1 else len_w

            # randomly select attributes from each category (should suffle the list first)
            # cannot handle the case where original/sampled attribute list is empty
            IsAttributes = ', '.join(sample(feature['IsAttributes'], c_i)).lower()[::]
            HasAttributes = ', '.join(sample(feature['HasAttributes'], c_h)).replace('_', ' ').lower()[::]
            WearAttributes = ', '.join(sample(feature['WearAttributes'], c_w)).replace('Wearing_', '').replace('_', ' ').lower()[::]

            # randomly select verbs for each category
            SelectWearAttributes = f'{choice(WearVerb)}{WearAttributes}'
            SelectHasAttributes = f'{choice(HaveVerb)}{HasAttributes}'
            SelectIsAttributes = f'{choice(subject)}{choice(IsVerb)}{IsAttributes}'

            # define caption formats here
            caption_format = {
                '1': f'{SelectIsAttributes}. {choice(subject)}{SelectHasAttributes} and{SelectWearAttributes}.',
                '2': f'{SelectIsAttributes} and{SelectHasAttributes}. {choice(subject)}{SelectWearAttributes}.',
                '3': f'This is a {IsAttributes} person. {choice(subject)}{SelectHasAttributes}. {choice(subject)}{SelectWearAttributes}.',
            }

            # randomly select one of the caption format
            random_format = choice(list(caption_format.keys()))
            caption = caption_format[random_format]
            captions.append(caption)

    return captions    


if __name__ == "__main__":

    anno_path = 'celeba-hq-attribute.txt'
    save_path = 'celeba_caption'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    with open(anno_path, 'r') as f:
        lines = f.readlines()
        num_images = int(lines[0])
        attributes = lines[1].split()
        # Store the attributes for each image in a dictionary
        image_attributes = {}
        for i in range(num_images):
            image_id, *attr_values = lines[i+2].split()
            image_attributes[image_id] = dict(zip(attributes, attr_values))

    for num in range (0, num_images):
        captions = get_caption(image_attributes['{}.jpg'.format(num)], NUM_CAPTION)
     
        with open('{}/{}.txt'.format(save_path, str(num)), "w") as f:
            f.write("\n".join(captions))

    print ('all done!') 

