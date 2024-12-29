from todoist_sh.args import parser


def run():
    args = parser.parse_args()
    args.func(args)
