import warnings
import utils

class LivingConfig(object):
    train_data_root = '/Users/Rudra/Downloads/deep_layout/pickle/train'
    val_data_root = '/Users/Rudra/Downloads/deep_layout/pickle/val'
    save_log_root = 'log'
    result_file = 'result_living.csv'
    module_name = 'living'
    model_name = 'resnet34_fc1'
    load_model_path = None
    load_connect_path = None 
    mask_size = 9 

    multi_GPU = False
    batch_size = 16
    num_workers = 2
    print_freq = 300

    max_epoch = 300
    current_epoch = 0    
    save_freq = 50
    val_freq = 5

    update_lr = True
    lr_decay_freq = 30
    lr_base = 1e-4  
    weight_decay = 1e-4

    def parse(self, kwargs, file):
        """
        根据字典kwargs 更新 config参数
        """
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning: opt has not attribut %s" % k)
            setattr(self, k, v)

        print('user config:')
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('__'):
                utils.log(file, f'{k}: {getattr(self, k)}')