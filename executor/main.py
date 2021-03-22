import datetime
import os
import argparse
import robot


def main():
    parser = argparse.ArgumentParser(description='+++ Script for test case execution +++',
                                     argument_default=argparse.SUPPRESS)
    parser.add_argument('file', help=f'file contains test suite need to be executed')
    parser.add_argument('--test', required=False, help=f'Test case name need to be executed')
    parser.add_argument("--include", action='append', required=False, help=f'Tag which will be included')
    parser.add_argument("--variable", action='append', required=False, help=f'Variable used for test suite')
    parser.add_argument("--browser", required=False, default='chrome', help=f'Browser is used to execute testing')
    parser.add_argument('-T', '--timestampoutputs', required=False, action='store_true', help=f'Output log based on timestamp')

    args = vars(parser.parse_args())

    if 'variable' not in list(args.keys()):
        args['variable'] = []
    args['variable'].append('browser:%s' % args['browser'])
    args.pop('browser')

    currentDate = datetime.datetime.now()
    sOutputDir = "../Report/%s" % currentDate.strftime("%d%m%Y")
    if not os.path.exists(sOutputDir):
        os.mkdir(sOutputDir)
    args['outputdir'] = sOutputDir
    robot.run(args['file'], **args)

if __name__ == "__main__":
    main()