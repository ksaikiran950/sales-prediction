from src.data_preprocessing import load_and_prepare_data
from src.train_model import train_and_save_model
from src.evaluate_model import evaluate_model

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_prepare_data("data/sales_data.csv")
    model = train_and_save_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)