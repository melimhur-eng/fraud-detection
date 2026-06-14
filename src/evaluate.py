from sklearn.metrics import (
    average_precision_score,
    f1_score,
    confusion_matrix
)

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
    else:
        y_prob = y_pred

    return {
        "AUC_PR": average_precision_score(y_test, y_prob),
        "F1": f1_score(y_test, y_pred),
        "Confusion_Matrix": confusion_matrix(y_test, y_pred)
    }