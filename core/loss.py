import torch
import torch.nn as nn


class AdversarialLoss(nn.Module):
    r"""
    Adversarial loss
    https://arxiv.org/abs/1711.10337
    """

    def __init__(
        self, type="nsgan", target_real_label=1.0, target_fake_label=0.0
    ) -> None:
        r"""
        type = nsgan | lsgan | hinge
        """
        super(AdversarialLoss, self).__init__()
        self.type = type
        self.register_buffer("real_label", torch.tensor(target_real_label))
        self.register_buffer("fake_label", torch.tensor(target_fake_label))

        if type == "nsgan":
            
