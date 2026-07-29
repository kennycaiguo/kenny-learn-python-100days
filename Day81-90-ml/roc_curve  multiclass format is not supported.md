The error `ValueError: multiclass format is not supported` occurs because **the \**\*\*[\*\*\*\*![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABH0lEQVR4AZSQPUvDUBSGHwId6iS6ufkb9E/4I7rq5qI/w9FFcHBQdOqgg9TFLYiDSBWEWvAjphappTbFfmmv91xJSkluml7uOefNPed9khtHzbp6LaUutpXaWzHhMMv6eoFiAZ4uI1d2QODD6ToEtcgsIhtgNITSFnQ/xTMR2QB3x9CsThjDh+kAeXv5KJyPVefk/gPXa9P9GcWa5sC7Svx009PJ2XE9Ns8fWTsss3vtx0Fvrh6z7+gKncEvB7d1CsUH/KA/djQqY52gIkDYe2712DirEGigOWu/mmJLMYAM1jsD9m/eRUI/+K+WnAiQ2VK1KWVqWAGN7yE1+Re5fCrEChCXXIX8gkhrpAKU0r75ZZ3sOxWwOJeDpVW7G/gDAAD//88rkXMAAAAGSURBVAMAUP2UBNIzD0gAAAAASUVORK5CYII=)\*\*\*\*⁠scikit-learn `roc_curve` function](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)\*\**\* only accepts binary targets**. You cannot pass multi-class labels (e.g., classes 0, 1, 2) directly into it. [[1](https://stackoverflow.com/questions/61114520/how-to-fix-valueerror-multiclass-format-is-not-supported), [2](https://stackoverflow.com/questions/61074634/how-to-solve-multiclass-format-is-not-supported-error-in-python), [3](https://github.com/pytorch/vision/issues/3250), [4](https://stackoverflow.com/questions/76265884/sklearn-valueerror-multiclass-format-is-not-supported)]

To resolve this, you must transform your data using a **One-vs-Rest (OvR)** approach, binarize your labels, and compute a separate ROC curve for every single class. [[1](https://stackoverflow.com/questions/73431559/roc-curve-multiclass-format-is-not-supported), [2](https://datascience.stackexchange.com/questions/115838/how-to-get-roc-curves-in-a-multi-label-scenario), [3](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)]

The Solution: One-vs-Rest Binarization

Use `label_binarize` from `sklearn.preprocessing` to convert your target labels into a binary matrix, and make sure you pass the **predicted probabilities** (`predict_proba`) rather than hard class predictions. [[1](https://github.com/scikit-learn/scikit-learn/discussions/25283), [2](https://dev.to/yakhilesh/65-roc-curves-and-auc-comparing-models-fairly-59j1), [3](https://stackoverflow.com/questions/73431559/roc-curve-multiclass-format-is-not-supported)]

python

```
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize

# 1. Define your classes (e.g., [0, 1, 2])
classes = [0, 1, 2]
n_classes = len(classes)

# 2. Binarize the true test labels (turns shape (N,) into (N, n_classes))
y_test_binarized = label_binarize(y_test, classes=classes)

# 3. Get predicted probabilities from your model (not hard class labels!)
# shape should be (N, n_classes)
y_score = model.predict_proba(X_test) 

# 4. Compute ROC curve and ROC area for each individual class
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    # Pass the column corresponding to the specific class
    fpr[i], tpr[i], _ = roc_curve(y_test_binarized[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# 5. Plot all ROC curves
plt.figure()
colors = ['blue', 'red', 'green']
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label=f'Class {classes[i]} (AUC = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Multiclass Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
plt.show()
```

 

Quick Troubleshooting Check

- **Are you passing the wrong metric name to a cross-validation tool?** If you saw this error while using `GridSearchCV` or `cross_val_score`, replace `scoring='roc_auc'` with `scoring='roc_auc_ovr'` or `scoring='roc_auc_ovo'`. [[1](https://stackoverflow.com/questions/76265884/sklearn-valueerror-multiclass-format-is-not-supported)]

- **Are you passing hard predictions?** Ensure you are feeding `model.predict_proba(X_test)` into your calculation, not `model.predict(X_test)`. ROC curves require continuous probability scores to sweep thresholds. [[1](https://dev.to/yakhilesh/65-roc-curves-and-auc-comparing-models-fairly-59j1), [2](https://python.plainenglish.io/understanding-classifier-performance-metrics-in-machine-learning-398bbf1442f8), [3](https://stats.stackexchange.com/questions/37795/roc-curve-for-discrete-classifiers-like-svm-why-do-we-still-call-it-a-curve), [4](https://github.com/scikit-learn/scikit-learn/discussions/25283)]

- **Just want a single evaluation metric number?** If you do not need the physical graph and only need the overall AUC score, skip `roc_curve` entirely. Use the built-in scikit-learn `roc_auc_score` function which natively supports multiclass data when specifying a strategy:

  python

  ```
  from sklearn.metrics import roc_auc_score
  # Computes One-vs-Rest AUC macro-average
  macro_auc = roc_auc_score(y_test, y_score, multi_class='ovr', average='macro')
  ```

   

   [[1](https://stackoverflow.com/questions/61074634/how-to-solve-multiclass-format-is-not-supported-error-in-python)]

If you are encountering this within a specific wrapper tool or framework, let me know **which machine learning library** you are using and **how your target variables are shaped**.



