import pandas as pd
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
df = pd.read_csv('Review.csv')

# Sample data
reviews = [
    "I loved this movie!", "Bad movie, didn't like it.",
    "Great acting!", "Worst experience.",
    "Good plot, great entertainment.",
    "Terrible acting, waste of money.",
    "Amazing plot, loved it!",
    "Very boring and slow.",
    "Excellent performance by actors.",
    "Didn't like the ending.",
    "Hilarious and entertaining!",
    "Predictable and dull.",
    "Loved the characters!",
    "Disappointing ending.",
    "Thrill ride, loved it!"
]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # 1: Positive, 0: Negative


# print(df['sentiment'].isnull().sum())
# print(df['sentiment'].unique())
# Preprocess
df['sentiment'] = df['sentiment'].map({'Positive': 1, 'Negative': 0})

# print(df['sentiment'].isnull().sum())

# Split
X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

# Vectorize
vectorizer = TfidfVectorizer(ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train
clf = LogisticRegression(class_weight='balanced', random_state=42)
clf.fit(X_train_vec, y_train)



# # Split data
# X_train, X_test, y_train, y_test = train_test_split(reviews, labels, test_size=0.2)

# # Vectorize text
# vectorizer = TfidfVectorizer(ngram_range=(1,2))
# X_train_vec = vectorizer.fit_transform(X_train)
# X_test_vec = vectorizer.transform(X_test)

# # Train classifier
# # clf = MultinomialNB()
# # clf.fit(X_train_vec, y_train)

# clf = LogisticRegression(class_weight='balanced')
# clf.fit(X_train_vec, y_train)

# Predict and evaluate
predictions = clf.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, predictions))

# Test on new text
new_text = ["This movie was fantastic!"]
new_vec = vectorizer.transform(new_text)
print("Sentiment:", clf.predict(new_vec))







# New review
new_review = ["This movie was a total waste of time!"]

# Vectorize the new review
new_review_vec = vectorizer.transform(new_review)

# Predict sentiment
prediction = clf.predict(new_review_vec)

# Print result
if prediction[0] == 1:
    print("Sentiment: Positive 😊")
else:
    print("Sentiment: Negative 😔")


print(labels.count(1), labels.count(0))




new_review = ["This movie was a totally fantastic!"]
new_review_vec = vectorizer.transform(new_review)
prediction = clf.predict(new_review_vec)

sentiment = "Positive 😊" if prediction[0] == 1 else "Negative 😔"
print("Sentiment:", sentiment)




with open('sentiment_model.pkl', 'wb') as f:
    pickle.dump(clf, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)




print("Model trained and saved!")

