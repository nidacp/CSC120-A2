from computer import *
from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory = []
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = inventory

    # What methods will you need?
    
    def buy(self, newComp):
        # "buys" new computer by adding it to the inventory array
        self.inventory.append(newComp)

    def sell(self, comp:Computer):
        # "sells" computer by removing it from inventory array
        self.inventory.remove(comp)

    # print full inventory
    def print_inventory(self):

    # number, all traits in brackets and commas
    # If the inventory is not empty
        if self.inventory.__len__() != 0:
            # For each item
            i=0
            computer:Computer
            for computer in self.inventory:
                # Print its details
                # description: str,
                #    processor_type: str,
                 #   hard_drive_capacity: int,
                  #  memory: int,
                   # operating_system: str,
                    #year_made: int,
                     #price: int
                print(f'Item ID: {i+1} : description: {computer.description}, processor type: { computer.processor_type}, hard drive capacity: {computer.hard_drive_capacity}, memory: {computer.memory}, operating system: {computer.operating_system}, year made: {computer.year_made}, price: {computer.price}')
                i+=1
        else:
            print("No inventory to display.")
