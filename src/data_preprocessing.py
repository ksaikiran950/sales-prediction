import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_prepare_data(filepath):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    df = df.drop(columns=["customer name", "customer e-mail", "country"])

    X = df.drop("car purchase amount", axis=1)
    y = df["car purchase amount"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test