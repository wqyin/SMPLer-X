import os
import os.path as osp

# will be update in exp
num_gpus = -1
exp_name = 'output/exp1/pre_analysis'

# quick access
save_epoch = 5
lr = 1e-5
end_epoch = 20
train_batch_size = 32

syncbn = True
bbox_ratio = 1.2

# continue
continue_train = False
start_over = True
# pretrained_model_path = '../output/train_gta_synbody_ft_20230410_132110/model_dump/snapshot_2.pth.tar'

# dataset setting
agora_fix_betas = True
agora_fix_global_orient_transl = True
agora_valid_root_pose = True

dataset_list = ['Human36M', 'MSCOCO', 'MPII', 'AGORA', 'EHF', 'SynBody', 'GTA_Human2', \
    'EgoBody_Egocentric', 'EgoBody_Kinect', 'UBody', 'PW3D', 'MuCo', 'PROX']
trainset_3d = []
trainset_2d = []
trainset_humandata = ['HumanSC3D']
testset = 'EHF'

# model
smplx_loss_weight = 1.0 #2 for agora_model for smplx shape
smplx_pose_weight = 10.0

smplx_kps_3d_weight = 100.0
smplx_kps_2d_weight = 1.0
net_kps_2d_weight = 1.0

agora_benchmark = 'agora_model' # 'agora_model', 'test_only'

model_type = 'osx_b'
encoder_config_file = 'transformer_utils/configs/osx/encoder/body_encoder_base.py'
encoder_pretrained_model_path = '../pretrained_models/osx_vit_b.pth'
feat_dim = 768

# model_type = 'osx_l'
# encoder_config_file = 'transformer_utils/configs/osx/encoder/body_encoder_large.py'
# encoder_pretrained_model_path = '../pretrained_models/osx_vit_l.pth'
# feat_dim = 1024

## =====FIXED ARGS============================================================
## model setting
upscale = 4
hand_pos_joint_num = 20
face_pos_joint_num = 72
num_task_token = 24
num_noise_sample = 0

## UBody setting
train_sample_interval = 10
test_sample_interval = 100
make_same_len = False

## input, output size
input_img_shape = (512, 384)
input_body_shape = (256, 192)
output_hm_shape = (16, 16, 12)
input_hand_shape = (256, 256)
output_hand_hm_shape = (16, 16, 16)
output_face_hm_shape = (8, 8, 8)
input_face_shape = (192, 192)
focal = (5000, 5000)  # virtual focal lengths
princpt = (input_body_shape[1] / 2, input_body_shape[0] / 2)  # virtual principal point position
body_3d_size = 2
hand_3d_size = 0.3
face_3d_size = 0.3
camera_3d_size = 2.5

## training config
print_iters = 100
lr_mult = 1

## testing config
test_batch_size = 32

## others
num_thread = 4
vis = False

## directory
output_dir, model_dir, vis_dir, log_dir, result_dir, code_dir = None, None, None, None, None, None
