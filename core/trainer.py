import os
import glob

from torch.utils.data import DataLoader
from torch.utils.data.distributed import DistributedSampler

from core.dataset import TrainDataset
from core.loss import AdversarialLoss


class Trainer:
    def __init__(self, config) -> None:
        self.config = config
        self.epoch = 0
        self.iteration = 0
        self.num_local_frames = config["train_data_loader"]["num_local_frames"]
        self.num_ref_frames = config["train_data_loader"]["num_ref_frames"]
        self.spynet_lr = config["trainer"].get("spynet_lr", 1.0)

        # setup data set and data loader
        self.train_dataset = TrainDataset(config["train_data_loader"])

        self.train_sampler = None
        self.train_args = config["trainer"]
        if config["distributed"]:
            self.train_sampler = DistributedSampler(
                self.train_dataset,
                num_replicas=config["world_size"],
                rank=config["global_rank"],
            )

        self.train_loader = DataLoader(
            self.train_dataset,
            batch_size=self.train_args["batch_size"] // config["world_size"],
            shuffle=(self.train_sampler is None),
            num_workers=self.train_args["num_workers"],
            sampler=self.train_sampler,
        )

        # set loss functions
        self.adversarial_loss = AdversarialLoss(type=self.config["losses"]["GAN_LOSS"])
