import sys
import os 
import argparse
from flask import Flask, render_template
import json 
from robot import run
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Visualizer.VisualizerListener import VisualizerListener
from Visualizer.ProcessTree import FlattenGraph


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", 
                            tree=tree_data, 
                            extra_inks=extra_links,
                            leaf_nodes = leaf_nodes,
                            show_labels = args['labels'])


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-s", "--suite", required=True, help="relative or absolute path to .robot file", type=str)
    arg_parser.add_argument("-l", "--labels", required=False, help="Option to show node labels", type=str2bool, default=False)
    arg_parser.add_argument("-ml", "--maxlevel", required=False, help="maximum testcase depth", type=int, default=None)
    arg_parser.add_argument("-ib", "--ignorebuiltin", required=False, help="Option to ignore builtin keywords", type=str2bool, default=True)
    args = vars(arg_parser.parse_args())

    listener = VisualizerListener(max_level=args['maxlevel'], ignore_builtin=args['ignorebuiltin'])
    options = {"log": None, "output": None, "report": None, 
               "listener": listener, "dryrun": "yes"}
    run(args['suite'], **options)

    trees = listener.trees
    fltten = FlattenGraph(trees[0])
    tree_data, extra_links, leaf_nodes = fltten.links, fltten.extra_links, fltten.leaf_nodes

    app.run(debug=True)
