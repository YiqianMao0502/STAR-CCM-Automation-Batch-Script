# STAR-CCM-Automation-Batch-Script
Meshes and Runs all .sim files in directory and sends Pushbullet notification on finish.
The script uses Expect to input the user password automatically between runs without the need for user intervention.

**System Requirements:** 
STAR-CCM+ v14 or higher
GNU/Linux Operating system
Python 3 
Expect Package Installed
Curl Package Installed
For notification functionality, make a Pushbullet account, generate a user token and install app on smartphone.

**Instructions**
1. Place all simulation files in the same directory as the script. (no need to generate volume mesh before hand).
2. Place the macro file "Meshandrun.java" in the same directory as the script.
3. From the terminal navigate to the script directory and run `python starccmAuto.py`

**Script Options** - at head of script
* starccmcommand: Terminal command to start STAR-CCM+.
* defuserpswd: Default user password. Can also be passed as an argument in script.
* pushbullettoken: Pushbullet user token from Pushbullet website.
* numofcores: Number of cores to run the simulations.
* macrofile: STAR-CCM+ macro file (Java) to be run before running simulation. Default: "meshandrun.java".
