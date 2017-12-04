#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Module de prise en charge des entrées/sorties, notamment pour
    la production et la consommation de fichiers ASCII.
    Usage:

    >>> from polyhash import say_hello
    >>> say_hello("World")
"""

import os
import sys

__all__ = ['getArgument','getExecutionDirectory']  # ajouter dans cette liste tous les symboles 'importables'

#repertoire d'excecution du script
execDirectory = os.getcwd()

#fichier passer en parametre (map a analyser)
Args = sys.argv
[execDirectory+"/"+ s for s in Args]
def getExecutionDirectory():
    return execDirectory
def getArgument():
    return Args
