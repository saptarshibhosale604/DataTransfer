####  timer.sh ####  
# e.g 
# timer.sh 1 sec
# timer.sh 2 min
# timer.sh 2        # sec default

#!/bin/bash 

# Check if the first argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <countdown_time> [sec|min]"
  	exit 1
fi

# Set the countdown time based on the first argument
countdown_time=$1

# Check the second argument for time unit
if [ "$2" == "min" ]; then
	countdown_time=$((countdown_time * 60))  # Convert minutes to seconds
elif [ "$2" != "sec" ] && [ -n "$2" ]; then
	echo "Invalid time unit. Use 'sec' for seconds or 'min' for minutes."
	exit 1
fi

# Use a C-style for loop for countdown
for (( i=countdown_time; i>=0; i-- )); do
	# Calculate minutes and seconds
	minutes=$((i / 60))
	seconds=$((i % 60))
	
	# Print in mm:ss format
	printf "\rCountdown: %02d:%02d" "$minutes" "$seconds"
	sleep 1
done

printf "\rCountdown: Time's up!      \n"  # Print the final message

####  stopwatch.sh ####  
#!/bin/bash

echo "Press [ENTER] to start the stopwatch"
read

start_time=$(date +%s)

echo "Stopwatch started. Press [ENTER] to stop."

# Loop to update the elapsed time
while true; do
	# Calculate elapsed time
	elapsed_time=$(( $(date +%s) - start_time ))
	
	# Convert elapsed time to hh:mm:ss format
	printf "\rElapsed time: %02d:%02d:%02d" $((elapsed_time / 3600)) $(( (elapsed_time % 3600) / 60 )) $((elapsed_time % 60))
	
	# Sleep for 1 second
	sleep 1
done &

# Wait for user to stop the stopwatch
read

# Kill the background process
kill $!

# Print final elapsed time
elapsed_time=$(( $(date +%s) - start_time ))
printf "\nFinal elapsed time: %02d:%02d:%02d\n" $((elapsed_time / 3600)) $(( (elapsed_time % 3600) / 60 )) $((elapsed_time % 60))


####  cmds.py ####  
free -h # RAM.
df -h # ROM
top -bn1 | grep "Cpu(s)" # CPU

####  fingersUpDownCount.py ####  

int fanSpeed = 0
# Fan speed control
if(up == 1):
	if(fanSpeed != 1):
        fanSpeed = 1 # Fan speed set to 1
        # Calling url
elif(up == 2):
    if(fanSpeed != 2):
        fanSpeed = 2 # Fan speed set to 2
        # Calling url
else:
    # Do nothing

  
