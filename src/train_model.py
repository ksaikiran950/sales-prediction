import pickle
from sklearn.ensemble import RandomForestRegressor

def train_and_save_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    return model