import torch
from torch.utils.data import TensorDataset, DataLoader
import numpy as np


def create_datasets(train_data: np.array, train_target: np.array,
                    test_data: np.array, test_target: np.array):
    """Converts NumPy arrays into PyTorch datasets."""

    trn_ds = TensorDataset(
        torch.tensor(train_data).float(),
        torch.tensor(train_target).long())
    tst_ds = TensorDataset(
        torch.tensor(test_data).float(),
        torch.tensor(test_target).long())
    return trn_ds, tst_ds


def create_loaders(data: TensorDataset, bs=128, jobs=0):
    """Wraps the datasets returned by create_datasets function with data loaders."""

    trn_ds, tst_ds = data
    trn_dl = DataLoader(trn_ds, batch_size=bs, shuffle=True, num_workers=jobs)
    tst_dl = DataLoader(tst_ds, batch_size=bs, shuffle=False, num_workers=jobs)

    return trn_dl, tst_dl

class DataBunch():
    def __init__(self, train_dl, test_dl):
        self.train_dl, self.test_dl = train_dl, test_dl

    @property
    def train_ds(self): return self.train_dl.dataset

    @property
    def test_ds(self): return self.test_dl.dataset