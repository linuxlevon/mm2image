import argparse

parser = argparse.ArgumentParser(description="Generate mermaid diagrams")
parser.add_argument(
    "filenames",
    nargs="+",
    metavar="FILENAME",
    help="file name(s) of mermaid diagram(s)",
)
parser.add_argument(
    "-c", "--clean", action="store_true", help="Clean all previous images"
)
args = parser.parse_args()
print(args)
filenames = args.filenames
clean = args.clean
print("filenames:", filenames)
print("clean:", clean)