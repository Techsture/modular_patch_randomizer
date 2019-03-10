#!/usr/bin/python

import argparse
import os
import random
import sys


MODULE_DIRECTORY = "./modules/"


def generate_audio_input_list():
  audio_input_list = []
  for module_file in os.listdir(MODULE_DIRECTORY):
    filename = MODULE_DIRECTORY + module_file
    with open(filename) as file:
      module_name = os.path.basename(filename)
      # For troubleshooting if files aren't loading:
      #print(module_name)
      for line in file.readlines():
        signal_type, jack_type, jack_name = line.split(' ')
        if signal_type is 'a' and jack_type is 'i':
          audio_input_list.append(module_name + " " + jack_name.strip('\n'))
    file.close()
  return audio_input_list


def generate_audio_output_list():
  audio_output_list = []
  for module_file in os.listdir(MODULE_DIRECTORY):
    filename = MODULE_DIRECTORY + module_file
    with open(filename) as file:
      module_name = os.path.basename(filename)
      # For troubleshooting if files aren't loading:
      #print(module_name)
      for line in file.readlines():
        signal_type, jack_type, jack_name = line.split(' ')
        if signal_type is 'a' and jack_type is 'o':
          audio_output_list.append(module_name + " " + jack_name.strip('\n'))
    file.close()
  return audio_output_list


def generate_cv_input_list():
  cv_input_list = []
  for module_file in os.listdir(MODULE_DIRECTORY):
    filename = MODULE_DIRECTORY + module_file
    with open(filename) as file:
      module_name = os.path.basename(filename)
      # For troubleshooting if files aren't loading:
      #print(module_name)
      for line in file.readlines():
        signal_type, jack_type, jack_name = line.split(' ')
        if signal_type is 'c' and jack_type is 'i':
          cv_input_list.append(module_name + " " + jack_name.strip('\n'))
    file.close()
  return cv_input_list


def generate_cv_output_list():
  cv_output_list = []
  for module_file in os.listdir(MODULE_DIRECTORY):
    filename = MODULE_DIRECTORY + module_file
    with open(filename) as file:
      module_name = os.path.basename(filename)
      # For troubleshooting if files aren't loading:
      #print(module_name)
      for line in file.readlines():
        signal_type, jack_type, jack_name = line.split(' ')
        if signal_type is 'c' and jack_type is 'o':
          cv_output_list.append(module_name + " " + jack_name.strip('\n'))
    file.close()
  return cv_output_list


def generate_patch(output_list, input_list, number_of_patches, longest_string_length):
  patch_list = []
  random.shuffle(output_list)
  random.shuffle(input_list)
  for i in range(1, number_of_patches):
    patch = ""
    output_choice = output_list.pop()
    #print(output_choice)
    input_choice = input_list.pop()
    #print(input_choice)
    padding_amount = longest_string_length - len(output_choice)
    padding = ""
    for i in range(0, padding_amount):
      padding += " "
    patch += output_choice + padding + " => " + input_choice
    patch_list.append(patch)
  return patch_list


def get_number_of_modules():
  number_of_modules = 0
  for module_file in os.listdir(MODULE_DIRECTORY):
    number_of_modules += 1
  return number_of_modules


def main():
  number_of_modules = get_number_of_modules()
  audio_output_list = generate_audio_output_list()
  number_of_audio_outputs = len(audio_output_list)
  audio_input_list = generate_audio_input_list()
  number_of_audio_inputs = len(audio_input_list)
  cv_output_list = generate_cv_output_list()
  number_of_cv_outputs = len(cv_output_list)
  cv_input_list = generate_cv_input_list()
  number_of_cv_inputs = len(cv_input_list)
  # More troubleshooting:
  #print("There are {} audio outputs and {} audio inputs.".format(number_of_audio_outputs, number_of_audio_inputs))
  #print("There are {} CV outputs and {} CV inputs.".format(number_of_cv_outputs, number_of_cv_inputs))
  number_of_audio_patches = min(number_of_audio_outputs, number_of_audio_inputs)
  number_of_cv_patches = min(number_of_cv_outputs, number_of_cv_inputs)
  # Even more troubleshooting:
  #print("The number of audio patches is {}.".format(number_of_audio_patches))
  #print("The number of complex cv patches is {}.".format(number_of_cv_patches))
  longest_audio_string_length = len(max(audio_output_list, key=len))
  longest_cv_string_length = len(max(cv_output_list, key=len))
  longest_string_length = max(longest_audio_string_length, longest_cv_string_length)
  audio_patch_list = generate_patch(audio_output_list, audio_input_list, number_of_audio_patches, longest_string_length)
  cv_patch_list = generate_patch(cv_output_list, cv_input_list, number_of_cv_patches, longest_string_length)
  audio_patch_list.sort()
  cv_patch_list.sort()
  # http://patorjk.com/software/taag/#p=display&h=1&v=1&f=Stop&t=Modular%0APatch%0ARandomizer
  print(""" ______              _         _                                   
|  ___ \            | |       | |                                  
| | _ | |  ___    _ | | _   _ | |  ____   ____                     
| || || | / _ \  / || || | | || | / _  | / ___)                    
| || || || |_| |( (_| || |_| || |( ( | || |                        
|_||_||_| \___/  \____| \____||_| \_||_||_|                        
 ______                    _                                       
(_____ \       _          | |                                      
 _____) )____ | |_   ____ | | _                                    
|  ____// _  ||  _) / ___)| || \                                   
| |    ( ( | || |__( (___ | | | |                                  
|_|     \_||_| \___)\____)|_| |_|                                  
 ______                     _                                     
(_____ \                   | |                                 
 _____) )  ____  ____    _ | |  ___   ____   _  _____  ____   ____ 
(_____ (  / _  ||  _ \  / || | / _ \ |    \ | |(___  )/ _  ) / ___)
      | |( ( | || | | |( (_| || |_| || | | || | / __/( (/ / | |    
      |_| \_||_||_| |_| \____| \___/ |_|_|_||_|(_____)\____)|_|    
                                                                   """)
  print("Your random patch is:\n")
  print("Audio:")
  for patch in audio_patch_list:
    print(patch)
  print("\nCV:")
  for patch in cv_patch_list:
    print(patch)
  exit()


if __name__ == '__main__':
  main()
