from agent import run
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-sessions", type=int, default=1)
parser.add_argument("-save", type=str, default=None)
parser.add_argument("-load", type=str, default=None)
parser.add_argument("-visual", type=str, choices=["on", "off"], default="on")
parser.add_argument("-dontlearn", action="store_true")
parser.add_argument("-step-by-step", action="store_true")
args = parser.parse_args()

run(args.sessions, args.load, args.save, args.dontlearn, args.visual, args.step_by_step, 2)
