import pandas as pd
from sklearn.preprocessing import StandardScaler
from server_side_tinder_swiper import tinder_api
from server_side_tinder_swiper import user_preferences

def process_user_data(user_data):
    user_data = pd.DataFrame(user_data)
    user_data = user_data.dropna()
    user_data = user_data.drop(['id'], axis=1)
    user_data = user_data.apply(lambda x: x.astype(str).str.lower())
    user_data = pd.get_dummies(user_data)
    return user_data

def get_user_features(user_id):
    user_data = tinder_api.get_user_data(user_id)
    processed_data = process_user_data(user_data)
    return processed_data

def update_user_preferences(user_id, preferences):
    user_preferences.update_preferences(user_id, preferences)

def get_user_preferences(user_id):
    preferences = user_preferences.get_preferences(user_id)
    return preferences

def scale_features(features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features