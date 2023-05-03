import os
import json


import torch
import torchvision.transforms as transforms

from core.utils import (Stack, ToTorchFormatTensor)

class TrainDataset(torch.utils.data.Dataset):
    def __init__(self, args: dict, debug=False):
        self.args = args
        self.num_local_frames = args["num_local_frames"]
        self.num_ref_frames = args["num_ref_frames"]
        self.size = self.w, self.h = (args["w"], args["h"])

        json_path = os.path.join(args["data_root"], args["name"], "train.json")
        with open(json_path, "r") as f:
            self.video_dict = json.load(f)
        self.video_names = list(self.video_dict.keys())
        if debug:
            self.video_names = self.video_names[:100]
        
        self._to_tensors = transforms.Compose([Stack(), ToTorchFormatTensor()])
