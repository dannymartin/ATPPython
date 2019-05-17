import oci
from oci.config import from_file
import atp, regions
import sys

"""
Example scripts demonstrating how to use the ATP Rest APIs for python

Usage:
python exampleUpdate.py cpuCoreCount dataStorageSizeTBs

"""


#Setup
#Verify the location of your OCI config file
config = from_file(file_location="/root/.oci/config")

try:

	#Example update body
	update = { "cpuCoreCount" : int(sys.argv[2]) ,
				"dataStorageSizeInTBs" : int(sys.argv[3])}

	exampleUpdate = atp.updateAutonomousDatabase(config, update, sys.argv[1])

	print("Response: " + str(exampleUpdate))
	print("Your database is being updated!")


except Exception as e: 
	print(e)