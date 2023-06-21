## Using the ChatGPT API on the Raspberry Pi

OpenAI has created an outstanding AI chatbot called ChatGPT, which can provide detailed and human-readable solutions to questions.
Since it has been taught from a large dataset, this AI knows quite a bit about many topics and can even produce code on command.

Although the Raspberry Pi cannot independently execute the ChatGPT model, it may communicate with an API that provides access to the AI service in the cloud.

In the following paragraphs, you will learn how to use your Raspberry Pi to communicate with ChatGPT via a Python script.

## Prerequisite

* Create an account via [OpenAI](https://auth0.openai.com/u/signup/identifier?state=hKFo2SA5OXpraVBiZVBEZTk1V1ZzNEw5eVRXRjVvdjBWeFd0SaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHBvUHozY013WS10YjFYUWtmMlhFYW1GUE91QnBVWmhzo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q), if you already have an account you can log in to obtain an API Key.

* Update your Raspberry Pi
```
sudo apt update
sudo apt upgrade
```

* Install Python PiP
```
sudo apt install python3 python3-pip
```

## Configuration

* Use PiP3 to install the OpenAI Python package
```
sudo pip3 install openai
```

To interact with ChatGPT from our Raspberry Pi, we will utilize the OpenAI Python module we installed earlier.

## Using Python on the Raspberry Pi to Interact with ChatGPT

* Begin to write Python script
```
nano chatgpt.py
```

* Modify [script provided](https://github.com/Ceceskii/PiProject350/blob/main/chatgpt.py) with your API Key provided on OpenAI. 
* When you have finished writing your script you can save and quit by pressing CTRL + X, followed by Y, then ENTER.

## Running

* Now that we have written the script, we can use it to start interacting with the ChatGPT AI from our Raspberry Pi. To run the script, you must run the following command in your terminal.
```
python3 chatgpt.py
```
* After the script is loaded, you will be prompted for you input. After input entered, ChatGPT will read the message sent from Raspberry Pi and then sent us the response.
  
![chatgpt](https://github.com/Ceceskii/PiProject350/assets/97866655/c98f40d4-7523-4c28-9385-c5329c0fb289)

## Citation
* This project is based on https://pimylifeup.com/raspberry-pi-chatgpt/ - It is a final project for CNE 350.

