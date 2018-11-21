#!/usr/bin/python

import os
import random
import sys


MODULE_DIRECTORY = "./modules/"


def generate_input_list():
  input_list = []
  for module_file in os.listdir(MODULE_DIRECTORY):
    filename = MODULE_DIRECTORY + module_file
    with open(filename) as file:
      module_name = os.path.basename(filename)
      for line in file.readlines():
        jack_type, jack_name = line.split(' ')
        if jack_type is 'i':
          input_list.append(module_name + " " + jack_name.strip('\n'))
    file.close()
  return input_list


def generate_output_list():
  output_list = []
  for module_file in os.listdir(MODULE_DIRECTORY):
    filename = MODULE_DIRECTORY + module_file
    with open(filename) as file:
      module_name = os.path.basename(filename)
      # For troubleshooting if files aren't loading:
      #print(module_name)
      for line in file.readlines():
        jack_type, jack_name = line.split(' ')
        if jack_type is 'o':
          output_list.append(module_name + " " + jack_name.strip('\n'))
    file.close()
  return output_list


def generate_patch(output_list, input_list, number_of_modules, longest_string_length):
  patch = ""
  random.shuffle(output_list)
  random.shuffle(input_list)
  for i in range(0, number_of_modules):
    output_choice = output_list.pop()
    input_choice = input_list.pop()
    padding_amount = longest_string_length - len(output_choice)
    padding = ""
    for i in range(0, padding_amount):
      padding += " "
    patch += output_choice + padding + " => " + input_choice + "\n"
  return patch


def get_number_of_modules():
  number_of_modules = 0
  for module_file in os.listdir(MODULE_DIRECTORY):
    number_of_modules += 1
  return number_of_modules


def main():
  number_of_modules = get_number_of_modules()
  output_list = generate_output_list()
  input_list = generate_input_list()
  longest_string_length = len(max(output_list, key=len))
  patch = generate_patch(output_list, input_list, number_of_modules, longest_string_length)
  print("Your random patch is:\n")
  print(patch)
  exit()


if __name__ == '__main__':
  main()