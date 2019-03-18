# rasa-framework-test

# Setup and installation
If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:

pip install -r requirements.txt
You also need to install a spaCy English language model. You can install it by running:

python -m spacy download en

# How to use this starter-pack?
NOTE: If running on Windows, you will either have to install make or copy the following commands from the Makefile
You can train the Rasa NLU model by running:
make train-nlu
This will train the Rasa NLU model and store it inside the /models/current/nlu folder of your project directory.

Train the Rasa Core model by running:
make train-core
This will train the Rasa Core model and store it inside the /models/current/dialogue folder of your project directory.

In a new terminal start the server for the custom action by running:
make action-server
This will start the server for emulating the custom action.

Test the assistant by running:
make cmdline
This will load the assistant in your terminal for you to chat.
