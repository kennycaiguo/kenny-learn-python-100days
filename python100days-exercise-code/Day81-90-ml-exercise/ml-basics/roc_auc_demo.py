import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelBinarizer
import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

matplotlib.use('TkAgg')

iris = load_iris()
target_names = iris.target_names
X,y = iris.data,iris.target
y = iris.target_names[y]

random_state = np.random.RandomState(0)
n_samples,n_features = X.shape
n_class = len(np.unique(y))
X = np.concatenate([X,random_state.randn(n_samples,200*n_features)],axis=1)
# X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.5,stratify=y,random_state=0)
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,stratify=y,random_state=0)

classifer = LogisticRegression()
y_score = classifer.fit(X_train,y_train).predict_proba(X_test)

label_binerizer = LabelBinarizer().fit(y_train)
y_onehot_test = label_binerizer.transform(y_test)
# print(y_onehot_test.shape)
# print(label_binerizer.transform(["virginica"]))
class_of_interest = "virginica"
class_id = np.flatnonzero(label_binerizer.classes_ == class_of_interest)[0]
print(class_id)
# ROC curve showing a specific class
display = RocCurveDisplay.from_predictions(
    y_onehot_test[:,class_id],
    y_score[:,class_id],
    name=f"{class_of_interest} vs the rest",
    curve_kwargs=dict(color='darkorange'),
    plot_chance_level=True,
    despine=True
)

_ = display.ax_.set(
    xlabel = 'False Positive Rate',
    ylabel = 'True Positive Rate',
     title="One-vs-Rest ROC curves:\nVirginica vs (Setosa & Versicolor)"
)

plt.show()