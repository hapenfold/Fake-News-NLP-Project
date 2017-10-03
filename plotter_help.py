import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
import itertools

def plot_explained_variance(svd, n_components,figsize=((14,8))):
    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(14,8))

    ax[0].plot(range(1, n_components), np.cumsum(svd.explained_variance_ratio_[1:]), lw=4, c='pink')
    ax[1].plot(range(1, n_components), svd.explained_variance_ratio_[1:], lw=4, c='seagreen')

    ax[0].set_title("\n Explained Variance of Singular Value Components \n", fontsize=20)
    ax[1].set_xlabel("\n Number of Truncations", fontsize=16)
    ax[0].set_ylabel("Eigenvalue \n", fontsize=16)
    ax[1].set_ylabel("Eigenvalue \n", fontsize=16)
    ax[0].legend(['Cumulative explained variance of text'], fontsize=14)
    ax[1].legend(['Explained variance of text'], fontsize=14)

    plt.show()


def sparse_matrix_plotter(head_sparse, body_sparse, markersize=0.2, precision=0, figsize=((12,6))):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize)

    ax1.spy(head_sparse, origin="lower", marker='.', markersize=markersize, precision=precision, c='seagreen')
    ax1.set_title("Visualisation of headline matrix sparcity \n\n", fontsize=16)
    ax1.tick_params(axis='x', labelsize=12)
    ax1.set_yticklabels([])


    ax2.spy(body_sparse, origin="lower", marker='.', markersize=markersize, precision=precision, c='seagreen')
    ax2.set_title("Visualisation of article body matrix sparcity \n", fontsize=16)
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])

    plt.show()

def plot_confusion_matrix(cm, classes, title='Confusion matrix\n', cmap=plt.cm.PuBuGn):
    plt.figure(figsize=(12,10))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=20)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    thresh = cm.max() / 2.

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label\n', fontsize=14)
    plt.xlabel('Predicted label\n', fontsize=14)
    plt.show()
