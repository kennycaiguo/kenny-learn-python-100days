import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelBinarizer
import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import roc_auc_score
from sklearn.metrics import auc, roc_curve
from itertools import cycle
from itertools import combinations

matplotlib.use('TkAgg')

iris = load_iris()
target_names = iris.target_names
X,y = iris.data,iris.target
y = iris.target_names[y]

random_state = np.random.RandomState(0)
n_samples,n_features = X.shape
n_class = len(np.unique(y))
X = np.concatenate([X,random_state.randn(n_samples,200*n_features)],axis=1)
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.5,stratify=y,random_state=0)
# X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,stratify=y,random_state=0)

classifer = LogisticRegression()
y_score = classifer.fit(X_train,y_train).predict_proba(X_test)

label_binerizer = LabelBinarizer().fit(y_train)
y_onehot_test = label_binerizer.transform(y_test)
# print(y_onehot_test.shape)
# print(label_binerizer.transform(["virginica"]))
class_of_interest = "virginica"
class_id = np.flatnonzero(label_binerizer.classes_ == class_of_interest)[0]
print(class_id)
# ROC curve using micro-averaged OvR
# display = RocCurveDisplay.from_predictions(
#     y_onehot_test.ravel(),
#     y_score.ravel(),
#     name="micro-average OvR",
#     curve_kwargs=dict(color='darkorange'),
#     plot_chance_level=True,
#     despine=True
# )

# _ = display.ax_.set(
#     xlabel = 'False Positive Rate',
#     ylabel = 'True Positive Rate',
#      title="Micro-averaged One-vs-Rest\nReceiver Operating Characteristic"
# )

# plt.show()

micro_roc_auc_ovr = roc_auc_score(
    y_test,
    y_score,
    multi_class='ovr',
    average='micro'
)

# print(f"Micro-averaged One-vs-Rest ROC AUC score:\n{micro_roc_auc_ovr:.2f}")
# 下面的代码和上面的代码是一样效果的
fpr,tpr,roc_auc = dict(),dict(),dict()
fpr["micro"],tpr["micro"],_ = roc_curve(y_onehot_test.ravel(),y_score.ravel())
roc_auc['micro'] = auc(fpr["micro"],tpr["micro"])

# print(f"Micro-averaged One-vs-Rest ROC AUC score:\n{roc_auc['micro']:.2f}")

for i in range(n_class):
    fpr[i],tpr[i],_ = roc_curve(y_onehot_test[:,i],y_score[:,i])
    roc_auc[i] = auc(fpr[i],tpr[i])

fpr_grid = np.linspace(0.0,1.0,1000)
# Interpolate all ROC curves at these points
mean_tpr = np.zeros_like(fpr_grid)
for i in range(n_class):
     # linear interpolation
    mean_tpr += np.interp(fpr_grid,fpr[i],tpr[i])
# Average it and compute AUC
mean_tpr /=n_class

fpr['macro'] = fpr_grid
tpr['macro'] = mean_tpr
roc_auc['macro'] = auc(fpr['macro'],tpr['macro'])
# print(f"Macro-averaged One-vs-Rest ROC AUC score:\n{roc_auc['macro']:.2f}")

macro_roc_auc_ovr = roc_auc_score(y_test,y_score,multi_class='ovr',average='macro')
# print(f"Macro-averaged One-vs-Rest ROC AUC score:\n{macro_roc_auc_ovr:.2f}")
  
# fig, ax = plt.subplots(figsize=(6, 6))

# plt.plot(
#     fpr["micro"],
#     tpr["micro"],
#     label=f"micro-average ROC curve (AUC = {roc_auc['micro']:.2f})",
#     color="deeppink",
#     linestyle=":",
#     linewidth=4,
# )

# plt.plot(
#     fpr["macro"],
#     tpr["macro"],
#     label=f"macro-average ROC curve (AUC = {roc_auc['macro']:.2f})",
#     color="navy",
#     linestyle=":",
#     linewidth=4,
# )

# colors = cycle(["aqua", "darkorange", "cornflowerblue"])
# for class_id, color in zip(range(n_class), colors):
#     RocCurveDisplay.from_predictions(
#         y_onehot_test[:, class_id],
#         y_score[:, class_id],
#         name=f"ROC curve for {target_names[class_id]}",
#         curve_kwargs=dict(color=color),
#         ax=ax,
#         plot_chance_level=(class_id == 2),
#         despine=True,
#     )

# _ = ax.set(
#     xlabel="False Positive Rate",
#     ylabel="True Positive Rate",
#     title="Extension of Receiver Operating Characteristic\nto One-vs-Rest multiclass",
# )

# plt.show()


# ROC curve using the OvO macro-average
"""
combinations in the Iris plants dataset: “setosa” vs “versicolor”, “versicolor” vs “virginica” and “virginica” vs “setosa”.
 Notice that micro-averaging is not defined for the OvO scheme.
"""
pair_list = list(combinations(np.unique(y),2))
# print(pair_list) # [(np.str_('setosa'), np.str_('versicolor')), (np.str_('setosa'), np.str_('virginica')), (np.str_('versicolor'), np.str_('virginica'))]
pair_scores = []
mean_tpr = dict()

for ix,(label_a,label_b) in enumerate(pair_list):
    a_mask = y_test == label_a
    b_mask = y_test == label_b
    ab_mask = np.logical_or(a_mask,b_mask)
    a_true = a_mask[ab_mask]
    b_true = b_mask[ab_mask]
    idx_a = np.flatnonzero(label_binerizer.classes_ == label_a)[0]
    idx_b = np.flatnonzero(label_binerizer.classes_ == label_b)[0]

    fpr_a,tpr_a ,_ = roc_curve(a_true,y_score[ab_mask,idx_a])
    fpr_b,tpr_b ,_ = roc_curve(b_true,y_score[ab_mask,idx_b])

    mean_tpr[ix] = np.zeros_like(fpr_grid)
    mean_tpr[ix] += np.interp(fpr_grid,fpr_a,tpr_a)
    mean_tpr[ix] += np.interp(fpr_grid,fpr_b,tpr_b)
    mean_tpr[ix] /=2
    mean_score = auc(fpr_grid,mean_tpr[ix])
    pair_scores.append(mean_score)

    # fig,ax = plt.subplots(figsize=(6,6))
    # plt.plot(
    #     fpr_grid,
    #     mean_tpr[ix],
    #     label=f"Mean {label_a} vs {label_b} (AUC = {mean_score:.2f})",
    #     linestyle=":",
    #     linewidth=4
    # )

    # RocCurveDisplay.from_predictions(
    #     a_true,
    #     y_score[ab_mask,idx_a],
    #     ax=ax,
    #     name=f"{label_a} as positive class"
    # )
    # RocCurveDisplay.from_predictions(
    #     b_true,
    #     y_score[ab_mask,idx_b],
    #     ax=ax,
    #     name=f"{label_b} as positive class",
    #     plot_chance_level=True,
    #     despine=True
    # )

    # ax.set(
    #     xlabel="False Positive Rate",
    #     ylabel="True Positive Rate",
    #     title=f"{target_names[idx_a]} vs {label_b} ROC curves",
    # )

    # print(f"Macro-averaged One-vs-One ROC AUC score:\n{np.average(pair_scores):.2f}")
    # plt.show()

macro_roc_auc_ovo = roc_auc_score(
    y_test,
    y_score,
    multi_class="ovo",
    average="macro",
)

print(f"Macro-averaged One-vs-One ROC AUC score:\n{macro_roc_auc_ovo:.2f}")    
    
# Plot all OvO ROC curves together
ovo_tpr = np.zeros_like(fpr_grid)

fig, ax = plt.subplots(figsize=(6, 6))
for ix, (label_a, label_b) in enumerate(pair_list):
    ovo_tpr += mean_tpr[ix]
    ax.plot(
        fpr_grid,
        mean_tpr[ix],
        label=f"Mean {label_a} vs {label_b} (AUC = {pair_scores[ix]:.2f})",
    )

ovo_tpr /= sum(1 for pair in enumerate(pair_list))

ax.plot(
    fpr_grid,
    ovo_tpr,
    label=f"One-vs-One macro-average (AUC = {macro_roc_auc_ovo:.2f})",
    linestyle=":",
    linewidth=4,
)
ax.plot([0, 1], [0, 1], "k--", label="Chance level (AUC = 0.5)")
_ = ax.set(
    xlabel="False Positive Rate",
    ylabel="True Positive Rate",
    title="Extension of Receiver Operating Characteristic\nto One-vs-One multiclass",
    aspect="equal",
    xlim=(-0.01, 1.01),
    ylim=(-0.01, 1.01),
)

plt.show()