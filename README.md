# HeadlineReader
An alexa skill to read out headlines from a supplied subreddit.

## Instructions
1. Install dependencies from requirements.txt with a
    ```
    pip install -r requirements.txt
    ```

2. Edit the python file with a valid reddit username and password to access the api.

3. Either host the python file on a valid https enabled server or use ngrok as a temporary host.

4. Set up your amazon developer account (This should be the same email as your alexa/amazon account.) with a skill and add the server address (either the ngrok subdomain or the domain where you hosted your file.)

5. Set up the intent with sample utterances for YesIntent and NoIntent.

6. Enable testing for skill on the developer account.

7. Run the python file and ngrok with a port of 5000 (if you're using ngrok).

8. Test on your Alexa device.

## WARNING
I do not own an Amazon echo to test this on. All testing was done on [echosim](https://echosim.io/). This should technically work on an echo too, if it doesn't and you'd like to help me test the program feel free to submit an issue or to messsage me.
