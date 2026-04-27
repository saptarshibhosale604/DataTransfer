# . "C:\Users\2261395\OneDrive - Cognizant\Projects\CMD\bat\shortcutFunction.ps1"

Function powershell {Start-Process powershell -ArgumentList "-noexit -file C:\Users\LENOVO\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1"}					# open powershell
Function cmd {Start-Process cmd}	# open cmd

Function rc {Restart-Computer}		# restart
Function stc {Stop-Computer} 		# shutdown

Function battery {wmic path Win32_Battery get EstimatedChargeRemaining		# battery percentage
	wmic path Win32_Battery get BatteryStatus								# Charging status
	echo "2: Charging ON"}	
Function sortbylength {ls | Sort-Object -Property Length -Descending} 		# Sort by length														

Function lsSize {											# Get ls of dir and files, hidden, with size, and total size, In tabular form
    $totalSize = 0  # Initialize total size variable
    $results = @()  # Initialize an array to hold output

    # Get all items (files and directories) in the current directory
    Get-ChildItem -Force | ForEach-Object {
		  $isHidden = ($_.Attributes -band [IO.FileAttributes]::Hidden) -ne 0
        
		  if ($_.PSIsContainer) {
            # If it's a directory, calculate its size
            $sizeMB = (Get-ChildItem $_.FullName -Recurse | Measure-Object Length -Sum).Sum / 1MB    
            $type = "Dir"
        } else {
            # If it's a file, get its size directly
            $sizeMB = $_.Length / 1MB
            $type = "File"
        }
			
 		  # Include hidden status in output
        if ($isHidden) {
            $type += "(h)"
        }

        # Add to results array
        $results += [PSCustomObject]@{
            Type = $type
            Name = $_.Name
            SizeMB = "{0:N2}" -f $sizeMB
        }

        # Add to total size
        $totalSize += $sizeMB  
    }

    # Output the results in tabular format
    $results | Format-Table -Property Type, Name, @{Label="SizeMB"; Expression={$_ | Select-Object -ExpandProperty SizeMB}; Alignment='Right'} -AutoSize


    # After the loop, write the total size to the console
    Write-Host ("Total Directory Size: {0:N2} MB" -f $totalSize)
}

# Git
Set-Alias git02 C:\Users\2261395\MinGit-2.47.0.2-64-bit\cmd\git.exe
Set-Alias git "C:\Users\2261395\ProjectWork\GitCli\MinGit-2.47.0.2-64-bit\cmd\git.exe"
# Set-Alias gits "C:\Users\2261395\ProjectWork\GitCli\MinGit-2.47.0.2-64-bit\cmd\git.exe status"
# Set-Alias gita "C:\Users\2261395\ProjectWork\GitCli\MinGit-2.47.0.2-64-bit\cmd\git.exe add"
# Set-Alias gitc "C:\Users\2261395\ProjectWork\GitCli\MinGit-2.47.0.2-64-bit\cmd\git.exe commit"
# Set-Alias gitp "C:\Users\2261395\ProjectWork\GitCli\MinGit-2.47.0.2-64-bit\cmd\git.exe push"

Set-Alias tf "C:\Users\2261395\Downloads\Software\Terraform\terraform.exe"
Set-Alias terraform "C:\Users\2261395\Downloads\Software\Terraform\terraform.exe"

Set-Alias psql "C:\Users\2261395\AppData\Local\Programs\pgAdmin 4\runtime\psql.exe"


function touch {
    param([string]$path)

    if (Test-Path $path) {
        # Update timestamp
        (Get-Item $path).LastWriteTime = Get-Date
    } else {
        # Create empty file
        New-Item -Path $path -ItemType File | Out-Null
    }
}

# Set-Alias touch touch

Function txtShortcutFunction {code "C:\Users\2261395\OneDrive - Cognizant\Projects\cmd\bat\shortcutFunction.ps1"} 

Function cdProjectWork {cd "C:\Users\2261395\ProjectWork"}

Function cdHMHGit {cd "C:\Users\2261395\Downloads\GitHMH"}
Function cdDbtRedshift {cd "C:\Users\2261395\Downloads\GitHMH\data-eng-dbt\"}
Function cdDbtSnowflake {cd "C:\Users\2261395\Downloads\GitHMH\data-eng-dbt-eap\"}
Function cdDbtSnowflakeSelectedModel {cd "C:\Users\2261395\Downloads\GitHMH\data-eng-automation\concourse\dbt_snowflake\"}
Function cdWeeklyTask {cd "C:\Users\2261395\Downloads\WeeklyTask\"}
Function cdMonthlyTask {cd "C:\Users\2261395\Downloads\MonthlyTask\"}
Function cdHMHClient {cd "C:\Users\2261395\OneDrive - Cognizant\Project HMH\HMH Client"}
Function codeLogseqPages {code "C:\Users\2261395\LOGSEG\pages\"}
Function pythonVPN {python "C:\Users\2261395\ProjectWork\Python\PythonVPNFiller\main.py"}

Function gitRefresh {
    param (
        [string]$InputBranch
    )
	
    Write-Host "`n...Checking repository status... : "
    Write-Host "git status :"
    git status

    Write-Host "`n...Checking out '$InputBranch' branch... : "
    Write-Host "git checkout $InputBranch :"
    git checkout $InputBranch

    Write-Host "`n...Checking repository status... : "
    Write-Host "git status :"
    git status

    Write-Host "`n...Pulling latest changes from origin... : "
    Write-Host "git pull upstream $InputBranch :"
    git pull upstream $InputBranch

    Write-Host "`n...Pushing changes to origin... : "
    Write-Host "git push :"
    git push

    Write-Host "`n...Checking repository status... : "
    Write-Host "git status :"
    git status
}

function gitPushNewBranch {
    param (
        [string]$branchName = $(Read-Host "Enter the new branch name"),
        [string]$commitMessage = $(Read-Host "Enter the commit message")
    )
    
    Write-Host "`n...Checking repository status... : "
    Write-Host "git status :"
    git status


    Write-Host "`n...Creating and switching to new branch '$branchName'..."
    Write-Host "git checkout -b $branchName :"
    git checkout -b $branchName

    Write-Host "`n...Checking repository status..."
    Write-Host "git status :"
    git status

    Write-Host "`n...Adding all changes..."
    Write-Host "git add . :"
    git add .

    Write-Host "`n...Checking repository status again..."
    Write-Host "git status :"
    git status

    Write-Host "`n...Committing changes with message '$branchName $commitMessage'..."
    Write-Host "git commit -m `"$branchName $commitMessage`" :"
    git commit -m "$branchName $commitMessage"

    Write-Host "`n...Final status before pushing..."
    Write-Host "git status :"
    git status
    
    Write-Host "`n...Pushing branch '$branchName' to remote 'fork'..."
    Write-Host "git push fork $branchName :"
    
    [string]$manInTheLoop = $(Read-Host "Should I push the branch?")
    
    git push fork $branchName

    Write-Host "`n...Final repository status..."
    Write-Host "git status :"
    git status
}


Function pythonDailyTask {python "C:\Users\2261395\ProjectWork\Python\PythonIBSDailyTask\main.py"}

Function pythonRoleAccess {python "C:\Users\2261395\ProjectWork\Snowflake\SnowSQL\roleAccess.py"}
Function startExcelRoleAccess {start "C:\Users\2261395\ProjectWork\Snowflake\SnowSQL\Data\history.py"}
Function cdRoleAccess {cd "C:\Users\2261395\ProjectWork\Snowflake\SnowSQL"}

Function pythonLakeFormation {python "C:\Users\2261395\ProjectWork\Python\LakeFormationGroup\main.py"}
Function startExcelLakeFormation {start "C:\Users\2261395\ProjectWork\Python\LakeFormationGroup\Data.xlsx"}
Function cdLakeFormation {cd "C:\Users\2261395\Downloads\GitHMH\data-eng-python-scripts\aws\lake-formation\jenkins-scripts\lake_formation_engine"}

Function pythonWaterBreak {Start-Process python "C:\Users\2261395\ProjectWork\Python\PythonWaterBreak\waterbreak03.py"}
Function pythonLLM {python "C:\Users\2261395\ProjectWork\Python\Python Gemini API\main04.py"}
Function pythonCircle {python "C:\Users\2261395\ProjectWork\Python\Python keep pc occupy\circle.py"}
Function pythonDarkMode {python "C:\Users\2261395\ProjectWork\Python\Python GUI Force Dark mode\main.py"}
Function pythonMDCalender {python "C:\Users\2261395\ProjectWork\Python\PythonTabularCalenderMaker\mdcal.py"}

function appLogseq {
    # Change directory to the Logseq application folder
    Write-Host "Changing directory to Logseq application folder"
    Write-Host "cmd: cd C:\Users\2261395\LogseqApp\Logseq"
    cd C:\Users\2261395\LogseqApp\Logseq

    # Rename the Logseq folder to Logseq.exe
    Write-Host "Renaming Logseq folder to Logseq.exe"
    Write-Host "cmd: mv .\Logseq .\Logseq.exe"
    mv .\Logseq .\Logseq.exe

    # Start the Logseq application
    Write-Host "Starting Logseq application"
    Write-Host "cmd: Start-Process .\Logseq.exe"
    Start-Process .\Logseq.exe

    # Rename Logseq.exe back to Logseq
    Write-Host "Renaming Logseq.exe back to Logseq"
    Write-Host "cmd: mv .\Logseq.exe .\Logseq"
    mv .\Logseq.exe .\Logseq

    # Change directory to the root
    Write-Host "Changing directory to root"
    Write-Host "cmd: cd /"
    cd /
}


Function GetFunctions {Get-Command -CommandType Function}	# get list of functions
Function GetCmdlets {Get-Command -CommandType cmdlet}		# get list of cmdlets
Function GetAliases {Get-Alias}								# get list of aliases

Function now {Get-Date -Format "ddd dd/MM/yyyy HH:mm:ss"}	# eg Sun 13-10-2024 18:24:26
	
