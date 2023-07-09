```python
import json

class UserPreferences:
    def __init__(self):
        self.preferences_file = "preferences.json"

    def get_preferences(self):
        try:
            with open(self.preferences_file, 'r') as file:
                preferences = json.load(file)
            return preferences
        except FileNotFoundError:
            return {}

    def update_preferences(self, new_preferences):
        preferences = self.get_preferences()
        preferences.update(new_preferences)
        with open(self.preferences_file, 'w') as file:
            json.dump(preferences, file)

    def get_preference(self, key):
        preferences = self.get_preferences()
        return preferences.get(key, None)

    def set_preference(self, key, value):
        preferences = self.get_preferences()
        preferences[key] = value
        self.update_preferences(preferences)
```