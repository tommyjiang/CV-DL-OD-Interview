import torch
import torchvision

def giou_loss(boxes1, boxes2, eps=1e-7):
    l1, t1, r1, b1 = boxes1.unbind(dim=-1)
    l2, t2, r2, b2 = boxes2.unbind(dim=-1)

    assert (r1 >= l1).all(), "bad box: r1 larger than l1"
    assert (b1 >= t1).all(), "bad box: b1 larger than t1"

    lmax = torch.max(l1, l2)
    tmax = torch.max(t1, t2)
    rmin = torch.min(r1, r2)
    bmin = torch.min(b1, b2)

    # 计算二者交、并
    intersect = torch.zeros_like(l1)
    mask = (bmin > tmax) & (rmin > lmax)
    intersect[mask] = (rmin[mask] - lmax[mask]) * (bmin[mask] - tmax[mask])

    union = (r1 - l1) * (b1 - t1) + (r2 - l2) * (b2 - t2) - intersect
    iou = intersect / (union + eps)

    # 最小外包矩形
    l = torch.min(l1, l2)
    r = torch.max(r1, r2)
    t = torch.min(t1, t2)
    b = torch.max(b1, b2)

    area_c = (r - l) * (b - t)
    miou = iou - (area_c - union) / (area_c + eps)

    loss = 1 - miou

    return loss


boxes1 = torch.Tensor([[1, 1, 5, 5], [1, 1, 10, 10]])
boxes2 = torch.Tensor([[0, 0, 10, 10], [0, 0, 10, 10]])
giou_loss = giou_loss(boxes1, boxes2)
tv_giou_loss = torchvision.ops.generalized_box_iou_loss(boxes1, boxes2)
assert giou_loss.eq(tv_giou_loss).any(), "GIoU loss mismatch!"
print(f'Self implemented GIoU loss: {giou_loss}')
print(f'Torchvision GIoU loss: {tv_giou_loss}')
