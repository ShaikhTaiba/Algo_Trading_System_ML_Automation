from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def train_model(df):
    df = df.dropna()
    df['Target'] = df['Close'].shift(-1) > df['Close']
    X = df[['RSI', '20DMA', '50DMA']].dropna()
    y = df['Target'][X.index]
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, accuracy