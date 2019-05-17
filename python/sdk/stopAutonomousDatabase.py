import oci
from oci.config import from_file
import atp, regions
import sys

"""
Example scripts demonstrating how to use the ATP Rest APIs for python

Usage:
python exampleStop.py stop OCID

Stops the database given the OCID
"""


#Setup
config = from_file(file_location="/root/.oci/config")

try:
	if len(sys.argv) == 2:
		
		exampleStop = atp.stopAutonomousDatabase(config, sys.argv[1])

		print("Response: " + str(exampleStop) )
		print("The instance is stopping!")


except Exception as e: 
	print(e)



