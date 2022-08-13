<#
Launcher for gallery-dl-difpy
Pseudo-executable script allowing for streamlined launching

To configure for local computer:
1. Change $repo string to location of gallery-dl-difpy folder on computer
2. Make a shortcut for this script for the desktop for ease of use
3. Configure the shortcut to run on click instead of opening up notepad
3a. Right click on shortcut and select properties
3b. In properties, prepend powershell.exe -ExecutionPolicy Bypass -File to the target field. Note that if there are spaces in the path, the path needs to be in quotes.
3c. If desired, rename shortcut

#>

# IMPORTANT: change repo path to where the app is stored on local computer
$repo = "C:\Users\Alex\Documents\Github\gallery-dl-difpy"
$current_dir = Get-Location

# Set working directory to repository
Set-Location -Path $repo


# Startup commands
.\venv\Scripts\Activate.ps1
python .\main.py

# Return to prior directory
Set-Location -Path $current_dir