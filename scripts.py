
#### cmds.py ####  
free -h # RAM.
df -h # ROM
top -bn1 | grep "Cpu(s)" # CPU
du -h --max-depth=1 # show size of current dir and subdir

du -h --max-depth=1 | sort -h	# size and sort
grim ~/Pictures/Screenshots/my_screenshot.png # screenshot

####  loggin.py ####  
import logging

def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="Logs/basic.log",
    )

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")

if __name__ == "__main__":
    main()


#### done chatbot.py ####
import TextToSpeech.textToSpeechOnline02 as TTS
import SpeechToText.speechToTextOnline as STT
import LLM.llm as LLM

debug01 = True

print("Initialized Chatbot")
userInput = "sleep" 	# sleep: Go to Hibernate
						# wakeUp: Goint to answer the user input
listWakeUpCalls = ["hey there", "hi there", "hey rpi"]
listSleepCalls = ["sleep now", "go to sleep", "we are done", "got it"]

roleDefining = f"""For the 'User Input' given below
answer as you are a 'JARVIS' from the 'Iron Man' movie
User Input = """

def Main():
	# Getting user input
	# userInput = "Hey there how its going on?" # sample 
	# userInput = input("userInput: ")	# Text 
	userInput = STT.Main()			# Speech To Text
	
	print("userInput:",userInput)	
	
	if (userInput is not None):
		if(debug01): print("userInput Not null")

		# Checking for wake up call
		if any(call in userInput.lower() for call in listWakeUpCalls):
	 		conversationMode = "wakeUp"
		# Checking for sleep call
	   	elif any(call in userInput.lower() for call in listSleepCalls):
	 		conversationMode = "sleep"

		if(debug01): print("conversationMode:",conversationMode)
		
		if (conversationMode == wakeUp):
			userInput = roleDefining + userInput			
			print("userInputWithDefinedRole:",userInput)

			# Getting responce from LLM model
			llmResponce = LLM.Main(userInput)	
			print("llmResponce:",llmResponce)

			# Text to speech
			TTS.Main(llmResponce)

while(True):
	Main()
	
#### done textToSpeech modification ####
import threading
import time
from gtts import gTTS
import os
from playsound import playsound

def text_to_speech(chunk):
    # Create a gTTS object for the chunk
    tts = gTTS(text=chunk, lang='en')
    # Save the audio to a temporary file
    tts.save("temp.mp3")
    # Play the audio file
    playsound("temp.mp3")
    # Optionally, remove the file after playing
    os.remove("temp.mp3")

def main():
    # Your large paragraph
    text = """This is a large paragraph that you want to convert to speech. 
    It contains multiple sentences and should be spoken in a natural manner. 
    The goal is to start speaking as soon as possible without waiting for the entire 
    text to be converted to audio. Let's break this down into smaller chunks 
    for better processing and playback."""

    # Split the text into chunks (you can adjust the size of the chunks)
    chunks = text.split('. ')  # Split by sentences for this example

    for chunk in chunks:
        # Start the TTS conversion in a separate thread for each chunk
        tts_thread = threading.Thread(target=text_to_speech, args=(chunk,))
        tts_thread.start()
        
        # Wait for the TTS thread to finish before moving to the next chunk
        tts_thread.join()

if __name__ == "__main__":
    main()

#### done timer.sh ####  
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

#### done  stopwatch.sh ####  
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



#### Done fingersUpDownCount.py ####  

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

  
