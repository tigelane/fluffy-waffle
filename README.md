# fluffy-waffle
Converts from a flat input configuration file into multiple networking device configuration files.

### Supported input file versions
* .1, .2

### Input
* Takes a YAML configuration file.  See example.yaml

#### Example Input file
```
version: .1
meta_data: 
  ticket_number: 239824
  customer_name: "DOR"

configuration_data: 
  # azure / aws
  cloud_provider: azure
  peering_type: vpn
  connection_type: 2930
  interface_description: "This will be created"
```

### Output
* 

### Usage
`./converter.py example.yaml`

### Steps to perform
1.  Validate input form the user - Make sure they enter a filename on the command line.
2.  Open the file - Make sure that the file exists.
3.  Read the contents and make sure it's YAML.
4.  Check the file / data format version.
5.  Read template file and output the new code file(s)

