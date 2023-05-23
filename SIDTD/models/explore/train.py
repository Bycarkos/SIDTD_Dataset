from SIDTD.models.Baseline.training_kfold_baseline import *
from SIDTD.models.arc_pytorch.train_coAttn import *
from SIDTD.models.transfg.train_kfold_transfg import *

from options.base_options import BaseOptions
from options.baseline_options import BaselineOptions
from options.trans_fg_options import TransFGOptions
from options.coaarn_options import CoAARNOptions

def init_logger(log_file='train.log'):
    from logging import getLogger, DEBUG, FileHandler, Formatter, StreamHandler
        
    log_format = '%(asctime)s %(levelname)s %(message)s'
        
    stream_handler = StreamHandler()
    stream_handler.setLevel(DEBUG)
    stream_handler.setFormatter(Formatter(log_format))
        
    file_handler = FileHandler(log_file)
    file_handler.setFormatter(Formatter(log_format))
        
    logger = getLogger('Herbarium')
    logger.setLevel(DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
        
    return logger 

def main(args):

    if args.model in ['vit_large_patch16_224', 'efficientnet-b3', 'resnet50']:
            
        # train model on all partition
        if args.type_split =='kfold':
            for iteration in range(args.nsplits):
                train_baseline_models(args, LOGGER, iteration)
        
        # train model on a specific partition
        else:
            train_baseline_models(args, LOGGER)
    

    if args.model == 'trans_fg':
            
        # train model on all partition
        if args.type_split =='kfold':
            for iteration in range(args.nsplits):
                train_transfg_models(args, LOGGER, iteration)
        
        # train model on a specific partition
        else:
            train_transfg_models(args, LOGGER)
        
    if args.model == 'coatten_fcn_model':

        # train model on all partition
        if args.type_split =='kfold':
            for iteration in range(args.nsplits):
                train_coAttn_models(args, iteration)
        
        # train model on a specific partition
        else:
            train_coAttn_models(args)


if __name__ == "__main__":


    parser = BaseOptions()
    args = parser.parse_args()

    if args.model in ['vit_large_patch16_224', 'efficientnet-b3', 'resnet50']:
        args = BaselineOptions(parser)

    elif args.model == 'trans_fg':
        args = TransFGOptions(parser)

    elif args.model == 'coatten_fcn_model':
        args = CoAARNOptions(parser)

    #global
    LOG_FILE = '{}_{}.log'.format(args.name, args.dataset) 
    LOGGER = init_logger(LOG_FILE)
        
    main(args)
