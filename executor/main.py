import datetime
import os
import argparse
import robot

parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('--test', type=str, required=False,
                    help='test case want to execute')
parser.add_argument('--file', type=str,
                    help='file contains test case want to execute')
parser.add_argument('-T','--timestampoutputs', nargs='?', type=bool, const=True, default=False)
args = vars(parser.parse_args())

def main():
    currentDate = datetime.datetime.now()
    sOutputDir = "../Report/%s" % currentDate.strftime("%d%m%Y")
    if not os.path.exists(sOutputDir):
        os.mkdir(sOutputDir)
    args['outputdir'] = sOutputDir
    robot.run(args['file'], **args)

if __name__ == "__main__":
    main()