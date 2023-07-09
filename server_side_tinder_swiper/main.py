```python
import tinder_api
import machine_learning_model
import data_processing
import message_sender
import user_preferences
import utils

def main():
    # Load user preferences
    preferences = user_preferences.get_preferences()

    # Get potential matches from Tinder API
    potential_matches = tinder_api.get_potential_matches()

    # Process the data of potential matches
    processed_data = data_processing.process_user_data(potential_matches)

    # Predict preferences for each potential match
    for user_data in processed_data:
        prediction = machine_learning_model.predict_preference(user_data)

        # If the prediction is positive, like the user and send a message
        if prediction == 1:
            tinder_api.like_user(user_data['id'])
            message = utils.format_message("What's going on?")
            message_sender.send_message(user_data['id'], message)

        # If the prediction is negative, dislike the user
        else:
            tinder_api.dislike_user(user_data['id'])

    # Update user preferences based on the interactions
    user_preferences.update_preferences(preferences)

if __name__ == "__main__":
    main()
```