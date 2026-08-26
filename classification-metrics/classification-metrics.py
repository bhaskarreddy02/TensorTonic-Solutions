import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    labels = np.unique(np.concatenate((y_true, y_pred)))

    precision = []
    recall = []
    f1 = []
    support = []

    for label in labels:

        tp = np.sum((y_true == label) & (y_pred == label))
        fp = np.sum((y_true != label) & (y_pred == label))
        fn = np.sum((y_true == label) & (y_pred != label))

        p = tp / (tp + fp) if tp + fp != 0 else 0
        r = tp / (tp + fn) if tp + fn != 0 else 0
        f = 2 * p * r / (p + r) if p + r != 0 else 0

        precision.append(p)
        recall.append(r)
        f1.append(f)
        support.append(np.sum(y_true == label))

    precision = np.array(precision)
    recall = np.array(recall)
    f1 = np.array(f1)
    support = np.array(support)

    if average == "macro":

        P = np.mean(precision)
        R = np.mean(recall)
        F = np.mean(f1)

    elif average == "weighted":

        weights = support / np.sum(support)

        P = np.sum(precision * weights)
        R = np.sum(recall * weights)
        F = np.sum(f1 * weights)

    elif average == "micro":

        tp = np.sum([
            np.sum((y_true == label) & (y_pred == label))
            for label in labels
        ])

        fp = np.sum([
            np.sum((y_true != label) & (y_pred == label))
            for label in labels
        ])

        fn = np.sum([
            np.sum((y_true == label) & (y_pred != label))
            for label in labels
        ])

        P = tp / (tp + fp) if tp + fp != 0 else 0
        R = tp / (tp + fn) if tp + fn != 0 else 0
        F = 2 * P * R / (P + R) if P + R != 0 else 0

    else:
        if pos_label in labels:
            i = np.where(labels == pos_label)[0][0]
            P = precision[i]
            R = recall[i]
            F = f1[i]
        else:
            P = R = F = 0

    accuracy = np.mean(y_true == y_pred)

    return {
        "accuracy": round(accuracy, 6),
        "precision": round(P, 6),
        "recall": round(R, 6),
        "f1": round(F, 6)
    }