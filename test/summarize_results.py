#! /usr/bin/env python3

import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input")
  parser.add_argument("-n", "--species_name")
  parser.add_argument("-o", "--output")
  args = parser.parse_args()

  gns = get_db_genes(args.input)
  with open(args.output, "w") as f:
    f.write(args.species_name+"\t")
    f.write(",".join(gns)+"\n")


def get_db_genes(pth):
  lst = []
  with open(pth) as f:
    for line in f:
      db = line.rstrip().split("\t")[1]
      lst.append(db)

  return list(set(lst))


if __name__ == "__main__":
  main()
