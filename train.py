from trainer import Trainer
from options import TrainOptions
from utils.workspace import load_config, merge_config
import paddle

if __name__ == "__main__":
    options = TrainOptions()
    opts = options.parse()
    if not opts.cfg:
        raise RuntimeError('No configuration file specified.')
    cfg = load_config(opts.cfg)
    if opts.data_path is not None:
        cfg['data_path'] = opts.data_path
    if opts.log_dir is not None:
        cfg['log_dir'] = opts.log_dir
    if opts.split is not None:
        cfg['split'] = opts.split
    if opts.num_gpus is not None:
        cfg['num_gpus'] = opts.num_gpus
    if opts.seed is not None:
        cfg['seed'] = opts.seed
    if opts.height is not None:
        cfg['height'] = opts.height
    if opts.width is not None:
        cfg['width'] = opts.width
    if opts.num_layers is not None:
        cfg['num_layers'] = opts.num_layers
    if opts.disparity_smoothness is not None:
        cfg['disparity_smoothness'] = opts.disparity_smoothness
    # cfg['scales'] = opts.scales
    # cfg['min_depth'] = opts.min_depth
    # cfg['max_depth'] = opts.max_depth
    # cfg['use_stereo'] = opts.use_stereo
    # cfg['frame_ids'] = opts.frame_ids
    if opts.use_depth_hints is not None:
        cfg['use_depth_hints'] = opts.use_depth_hints
    if opts.depth_hint_path is not None:
        cfg['depth_hint_path'] = opts.depth_hint_path
        
    # cfg['scheduler_step_size'] = opts.scheduler_step_size
    # cfg['weights_init'] = opts.weights_init
    if opts.model_name is not None:
        cfg['model_name'] = opts.model_name
    if opts.num_workers is not None:
        cfg['num_workers'] = opts.num_workers
    if opts.batch_size is not None:
        cfg['batch_size'] = opts.batch_size
    if opts.learning_rate is not None:
        cfg['learning_rate'] = opts.learning_rate
    if opts.start_epoch is not None:
        cfg['start_epoch'] = opts.start_epoch
    if opts.num_epochs is not None:
        cfg['num_epochs'] = opts.num_epochs
    if opts.scheduler_step_size is not None:
        cfg['scheduler_step_size'] = opts.scheduler_step_size
    if opts.load_weights_folder is not None:
        cfg['load_weights_folder'] = opts.load_weights_folder
    if opts.models_to_load is not None:
        cfg['models_to_load'] = opts.models_to_load
    if opts.log_frequency is not None:
        cfg['log_frequency'] = opts.log_frequency
    if opts.save_frequency is not None:
        cfg['save_frequency'] = opts.save_frequency
    if opts.visualdl_frequency is not None:
        cfg['visualdl_frequency'] = opts.visualdl_frequency


    merge_config(opts.opt)
    # disable npu in config by default
    if 'use_npu' not in cfg:
        cfg.use_npu = False

    # disable xpu in config by default
    if 'use_xpu' not in cfg:
        cfg.use_xpu = False

    if cfg.use_gpu:
        place = paddle.set_device('gpu')
    elif cfg.use_npu:
        place = paddle.set_device('npu')
    elif cfg.use_xpu:
        place = paddle.set_device('xpu')
    else:
        place = paddle.set_device('cpu')

    if 'norm_type' in cfg and cfg['norm_type'] == 'sync_bn' and not cfg.use_gpu:
        cfg['norm_type'] = 'bn'

    # # FIXME: Temporarily solve the priority problem of FLAGS.opt
    # merge_config(opts.opt)
    # check.check_config(cfg)
    # check.check_gpu(cfg.use_gpu)
    # check.check_npu(cfg.use_npu)
    # check.check_version()

    print(cfg)
    trainer = Trainer(cfg)
    trainer.train()