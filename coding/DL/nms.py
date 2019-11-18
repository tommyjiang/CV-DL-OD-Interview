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
    """
    boxes: N row with [x1, y1, x2, y2, score] format
    """
    N = len(boxes)
    i = 0
    while i < N:
        max_score = boxes[i, 4]
        max_pos = i

        # pick the bbox with maximum score
        for pos in range(i+1, N):
            if boxes[pos, 4] > max_score:
                max_score = boxes[pos, 4]
                max_pos = pos

        for ind in range(5):
            boxes[max_pos, ind], boxes[i, ind] = boxes[i, ind], boxes[max_pos, ind]

        tx1, ty1, tx2, ty2, ts = boxes[i, 0], boxes[i, 1], boxes[i, 2], boxes[i, 3], boxes[i, 4]

        pos = i + 1
        while pos < N:
            x1, y1, x2, y2, s = boxes[pos, 0], boxes[pos, 1], boxes[pos, 2], boxes[pos, 3], boxes[pos, 4]
            w = min(tx2, x2) - max(tx1, x1) + 1
            h = min(ty2, y2) - max(ty1, y1) + 1

            if w > 0 and h > 0:
                iou = w * h / ((tx2 - tx1 + 1) * (ty2 - ty1 + 1) + (x2 - x1 + 1) * (y2 - y1 + 1) - w * h)
                weight = np.exp(-(iou * iou)/sigma)

            boxes[pos, 4] *= weight
            if boxes[pos, 4] < thresh:
                # swap with last bbox
                for ind in range(5):
                    boxes[pos, i] = boxes[N-1, i]
                N -= 1
                pos -= 1

            pos += 1
        i += 1

    keep = [i for i in range(N)]
    return keep
