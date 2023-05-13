import sys
import shutil

if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    dir = sys.argv[1]
    # print("dir: ", dir)
    shutil.rmtree(dir)
