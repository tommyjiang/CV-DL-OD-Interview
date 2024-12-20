import torch
import torch.nn.functional as F


def sigmoid_focal_loss(
    inputs: torch.Tensor,
    targets: torch.Tensor,
    alpha: float = 0.25,
    gamma: float = 2,
    ):
    """
    Loss used in RetinaNet for dense detection: https://arxiv.org/abs/1708.02002.

    Args:
        inputs (Tensor): A float tensor of arbitrary shape.
                The predictions for each example.
        targets (Tensor): A float tensor with the same shape as inputs. Stores the binary
                classification label for each element in inputs
                (0 for the negative class and 1 for the positive class).
        alpha (float): Weighting factor in range (0,1) to balance
                positive vs negative examples or -1 for ignore. Default: ``0.25``.
        gamma (float): Exponent of the modulating factor (1 - p_t) to
                balance easy vs hard examples. Default: ``2``.
    Returns:
        Loss tensor with the reduction option applied.
    """
    p = torch.sigmoid(inputs)
    # ce_loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction='none')
    ce_loss = - (targets * torch.log(p) + (1 - targets) * torch.log(1 - p))
    p_t = p * targets + (1 - p) * (1 - targets)
    loss = ce_loss * ((1 - p_t) ** gamma)

    if alpha >= 0:
        alpha_t = alpha * targets + (1 - alpha) * (1 - targets)
        loss = alpha_t * loss

    loss = loss.mean()

    return loss

inputs = torch.tensor([[1.1, -2.0, 3.4], [-2.4, 3.9, -4.7]])
targets = torch.tensor([[0.0, 1.0, 0.0], [1.0, 0.0, 1.0]])

loss = sigmoid_focal_loss(inputs, targets)
print(loss)
