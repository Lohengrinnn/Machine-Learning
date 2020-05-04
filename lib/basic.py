#!/usr/bin/env python
# coding: utf-8

# In[7]:

import math

def isnum(val):
    """Return if an object is number.

    >>> [isnum(n) for n in [1, 1.2, "1.2", None]]
    [True, True, False, False]
    """
    return type(val) is int or type(val) is float

def mean(arr):
    """Return the mean of an array, expect non-number.
    >>> [mean(arr) for arr in [[1,2], [1,2,None]]]
    [1.5, 1.5]
    >>> mean([1,2,"String"])
    Traceback (most recent call last):
    ...
    TypeError
    """
    cum = 0.0
    cnt = 0.0
    for val in arr:
        if isnum(val):
            cum += val
            cnt += 1
        elif val:
            print("val %s type is %s", val, type(val))
            raise TypeError
    return cum / cnt

def dot(x, w):
    """Return the dot product of two vectors.
    >>> dot({"A": 3, "B": 4}, {"A": 3, "B": 4})
    25.0
    >>> dot({"A": 3, "B": 4}, {"C": 3, "D": 4})
    0.0
    """
    res = 0.0
    for key, val in x.items():
        if isnum(val):
            res += val * w.get(key, 0.0)
    return res


def norm(w):
    """Return L1 norm of an vector
    >>> norm({"A": 3, "B": 4})
    5.0
    """
    return math.sqrt(dot(w, w))

def class_distribution(examples):
    """Return dict divided by class("label")
    >>> class_distribution([{"label": 1}, {"label": 1}, {"label": 0}, {"label": 0}])
    {1: 0.5, 0: 0.5}
    """
    size = len(examples)
    if size == 0:
        raise Exception("zero example")
    dist = {}
    for example in examples:
        label = example["label"]
        dist[label] = dist.get(label, 0.0) + 1.0
    for key, val in dist.items():
        dist[key] = val / size
    return dist

def entropy(dist):
    """Return entropy of a distribution
    >>> entropy({1: 0.5, 0: 0.5})
    0.6931471805599453
    """
    e = 0.0
    for v in dist.values():
        if (1 >= v > 0):
            e -= v * math.log(v)
    return e

def information_gain(h0, splits):
    total = sum(len(split) for split in splits.values())
    e = 0.0
    for split in splits.values():
        e += (len(split) * entropy(class_distribution(split)) / total)
    return h0 - e

def assert_in_delta(a, b, delta, description = None):
    if not abs(a - b) < delta:
        if description: print(description)
        assert(False)

def assert_equal(val, expect):
    assert(val == expect)

class Metric:
    def apply(self, scores):
        pass

class AUCMetric(Metric):
    def roc_curve(self, scores):
        # scores = [[score, label]]
        # BEGIN YOUR CODE
        auc = 0.0
        tp_rates = [0.0]
        fp_rates = [0.0]
        tp_i = 0
        fp_i = 0
        p_total = sum(1 if label > 0 else 0 for score, label in scores)
        f_total = len(scores) - p_total
        for score, label in sorted(scores, key=lambda row: -row[0]):
            if label > 0:
                tp_i += 1
            else:
                fp_i += 1

            tp_rates.append(tp_i / p_total)
            fp_rates.append(fp_i / f_total)
            auc += ((fp_rates[-1] - fp_rates[-2]) * (tp_rates[-1] + tp_rates[-2]) / 2)

        return [fp_rates, tp_rates, auc]

    def apply(self, scores):
        fp, tp, auc = self.roc_curve(scores)
        return auc


if __name__ == "__main__":
    import doctest
    doctest.testmod()