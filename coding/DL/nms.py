import numpy as np

def nms():
    """
    bbox: n row with [x1, y1, x2, y2, score] format
    """
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    scores = dets[:, 4]
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        intersection = w * h
        iou = intersection / (areas[i] + areas[order[1:]] - intersection)

        inds = np.where(iou <= thresh)[0]
        order = order[inds + 1]
    return keep


def soft_nms():
    pass
