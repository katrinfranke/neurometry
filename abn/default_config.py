"""Default configuration for a run."""

import logging
from datetime import datetime
from platform import architecture

import torch

run_name = "trial run"

# Can be replaced by logging.DEBUG or logging.WARNING
logging.basicConfig(level=logging.INFO)

# Hardware
device = "cuda" if torch.cuda.is_available() else "cpu"

# Training
batch_size = 128  # 128
log_interval = 10
checkpt_interval = 10
n_epochs = 100
learning_rate = 1e-3
beta = 1.0
alpha = 100.0
gamma = 100.0

timestep_microsec = -1
expt_id = -1
# Dataset
dataset_name = "wiggles"
if dataset_name == "experimental":
    expt_id = "34"  # hd: with head direction
    timestep_microsec = 1000000

if dataset_name in ["images", "projected_images"]:
    img_size = 64

amp_wiggles = -1
if dataset_name == "wiggles":
    amp_wiggles = 0

# Models
model_type = "fc_vae"
encoder_width = 400
decoder_width = 400
encoder_depth = 3
decoder_depth = 3
latent_dim = 2
posterior_type = "gaussian"
gen_likelihood_type = "gaussian"
with_regressor = False
if with_regressor:
    weight_regressor = 1.0
    h_dim_regressor = 20

# Results
now = str(datetime.now().replace(second=0, microsecond=0))
results_prefix = f"{dataset_name}_{now}"
trained_model_path = None
