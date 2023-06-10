#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for sub_mtx in matrix:
        print(" ".join("{:d}".format(elt) for elt in sub_mtx))
