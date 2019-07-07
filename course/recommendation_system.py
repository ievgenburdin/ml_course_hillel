from joblib import load

classification_model = load("model.joblib")

while True:
    grades = [int(g) for g in input("ENTER SPACE SEPARATED TECHNICAL AND ENGLISH GRADES").split()]
    X = [grades]
    model_responce = classification_model.predict(X)[0]
    model_confidence = classification_model.predict_proba(X)[0][1]
    if model_responce == 0:
        text_resp = "fails"
    elif model_responce == 1:
        text_resp = "passes"
    resp_confidence = int(round(abs(200 * model_confidence - 100)))
    print(f"RESP {text_resp} CONFIDENCE {resp_confidence}")
