# STAR-CCM-Automation-Batch-Script
Meshes and Runs all .sim files in directory and sends Pushbullet notification on finish.
The script uses Expect to input the user password automatically between runs without the need for user intervention.

**System Requirements:** 
STAR-CCM+ v14 or higher
GNU/Linux Operating system
Python 2/3 
Expect Package Installed
Curl Package Installed

For notification functionality, make a free Pushbullet account, generate a user token and install app on smart phone.

**Instructions**
1. Place all simulation files in the same directory as the script. (no need to generate volume mesh before hand)
2. Place the macro file "Meshandrun.java" in the same directory as the script.
3. From the terminal navigate to the script and run "python XXXXX.py"



