#! /usr/bin/env python3

import sys
import yaml

SUPPORTED_VERSIONS = [.1, .2]

class VersionError(Exception):
    pass

def check_version(version):
    if version not in SUPPORTED_VERSIONS:
        raise VersionError(f"Configuration file version: {version} not in supported list: {SUPPORTED_VERSIONS}")

    return
    
def open_file(input_filename):
    try:
        # Open the file for read access only
        with open(input_filename, 'r') as input_file:
            # Use the yaml module to convert the file to a usable form
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            conversion_data = yaml.load(input_file, Loader=yaml.FullLoader)

    except OSError:
        print (f"Could not read file: {input_filename}")
    except KeyError as my_error:
        print (f"Data object missing in file: {my_error}")
        input_file.close()

    input_file.close()
    return conversion_data

def main(input_filename):
    # Make sure we have the right file name here
    print (f"Asking for file name: {input_filename}")

    # Open the file and get the information
    conversion_data = open_file(input_filename)

    # Make sure the configuration file version is accpetable
    check_version(conversion_data["version"])

    print (conversion_data)

if __name__ == "__main__":
    # Check our input to look for 1 argument
    if len(sys.argv) != 2:
        # Raise an error if we don't have the right number
        raise SyntaxError("Insufficient arguments.  Please provide a variables input file name.")
        exit()
    else:
        # Start the conversion by sending the filename to the main function 
        main(sys.argv[1])




