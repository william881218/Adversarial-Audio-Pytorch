from argparse import ArgumentParser

from asr_attack import AsrAttack


def main(args):

    attack_params = {
        'global_max_length':30000,
        'initial_eps':0.0001,
        'max_iter_1st_stage':400,
        'max_iter_2nd_stage':100,
        'learning_rate_1st_stage':0.000001,
        'learning_rate_2nd_stage':0.0000001,
        'initial_rescale':1.0,
        'rescale_factor':0.9,
        'num_iter_adjust_rescale':20,
        'initial_alpha':0.01,
        'increase_factor_alpha':1.2,
        'num_iter_increase_alpha':20,
        'decrease_factor_alpha':0.8,
        'num_iter_decrease_alpha':20,
        'batch_size':1,
        'use_amp':True,
        'opt_level':"O1",
    }

    my_asr_attack = AsrAttack(**attack_params)
    my_asr_attack.generate_adv_example(input_path=args.input_path, 
                                       target=args.target, 
                                       output_path=args.output_path)


def set_parser():

    parser = ArgumentParser()

    # data directories
    parser.add_argument("-i", "--input_path", type=str, default="/home/b07902027/AudioMNIST/data/01/1_01_0.wav")
    parser.add_argument("-t", "--target", type=str, default="SEVEN")
    parser.add_argument("-o", "--output_path", type=str, default="/home/b07902027/adversarial_asr_pytorch/adv_example/out.wav")

    return parser.parse_args()


if __name__ == '__main__':
    args = set_parser()
    main(args)
