import joblib

def save_model(model, filepath):
    try:
        joblib.dump(model, filepath)
        print(f"Model saved to {filepath}")
    except Exception as e:
        print(f"Error saving model: {e}")