# STAR-CCM-Automation-Batch-Script
Meshes and Runs all .sim files in directory and sends Pushbullet notification on finish.
The script uses Expect to input the user password automatically between runs without the need for user intervention.

**System Requirements:** 
STAR-CCM+ v14 or higher
GNU/Linux Operating system
Python 3 
Expect Package Installed
Curl Package Installed
For notification functionality, make a free Pushbullet account, generate a user token and install app on smartphone.

**Instructions**
1. Place all simulation files in the same directory as the script. (no need to generate volume mesh before hand).
2. Place the macro file "Meshandrun.java" in the same directory as the script.
3. From the terminal navigate to the script and run `python XXXXX.py`

*Script Options - at head of script
*starccmcommand: Terminal Command to start STAR-CCM+.
*defuserpswd: Default user password.
*pushbullettoken: Pushbullet User Token form Pushbullet website.
*numofcores: number of cores to run the simultions.
*macrofile: STAR-CCM+ macro file (Java) to be run before running sim. Default is "meshandrun.java".
