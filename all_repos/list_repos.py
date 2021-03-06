import argparse

from all_repos import cli
from all_repos.config import load_config


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='List all cloned repository names.',
        usage='all-repos-list-repos [options]',
    )
    cli.add_common_args(parser)
    args = parser.parse_args(argv)

    config = load_config(args.config_filename)
    for repo in config.get_cloned_repos():
        print(repo)


if __name__ == '__main__':
    exit(main())
