def predict_price(model, area, bedrooms, bathrooms):
    return model.predict([[area, bedrooms, bathrooms]])[0]
