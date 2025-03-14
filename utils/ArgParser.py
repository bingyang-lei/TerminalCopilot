import argparse
def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', default="qwen2.5",help="Designate a model to use, default is qwen2.5") # llama3.2:1b, llama3.1:8b, qwen2.5, deepseek-r1:32b
    parser.add_argument('--model2', help="(option) Choosing another model to talk with final model") # llama3.2:1b, llama3.1:8b, qwen2.5, deepseek-r1:32b
    parser.add_argument('-r', '--reasoning', action='store_true', help="Enable reasoning mode(more powerful but slower)")
    parser.add_argument("-p", "--ppt", action="store_true", help="进入PPT制作模式")
    parser.add_argument('-t', '--talk', nargs=2, metavar=('PROMPT', 'ROUNDS'), 
                        help='Start dialogue mode with initial prompt and max rounds')
    return parser.parse_args()