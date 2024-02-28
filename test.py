# NBMultinomial
data_train = pd.read_csv(r"Training.csv")

X = data_train.drop("prognosis", axis=1)
y = data_train["prognosis"]
# print(X)
# input()
test_data = pd.read_csv(r"Testing.csv")
X_test = test_data.drop("prognosis", axis=1)
y_test = test_data["prognosis"]
model = NBMultinomial()
model.train_data(X, y)

y_pred = model.predict(X_test)
print(y_pred)
point = model.score(y_pred, y_test)
print(point)

# LabelEncoder

X = data.drop("v1", axis=1)
y = data["v1"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0018, random_state=40552, stratify=y)
lab = label_encoder()
lab.train(X_train)

transformed_train_data = lab.transform(X_train)
