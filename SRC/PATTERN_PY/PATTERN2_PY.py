"""PATTERN2_PY.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     PATTERN_PY
 Module:
     PATTERN2_PY.py
 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
# Получить текущий рабочий каталог
current_directory = os.getcwd ()
import textwrap
import sys
import stat

import chardet
from chardet.universaldetector import UniversalDetector
from charset_normalizer import detect

import logging

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU
#------------------------------------------
import lyrpy.LULog as LULog
import lyrpy.LUConst as LUConst
import lyrpy.LUParserARG as LUParserARG

#------------------------------------------
# CONST
#------------------------------------------

#------------------------------------------
# sys.argv[1] - a1
# sys.argv[2] - a2
# sys.argv[3] - a3
#------------------------------------------
def main ():
    global Gwidth
#beginfunction
    LUConst.SET_LIB(__file__)

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'console', LUConst.GDirectoryLOG, LUConst.GFileNameLOG,
                        LUConst.GFileNameLOGjson)
    LULog.LoggerTOOLS.level = logging.INFO

    LArgParser = LUParserARG.TArgParser (description = 'Параметры', prefix_chars = '-/')
    LArg = LArgParser.ArgParser.add_argument ('a1', type = str, default='', help = 'a1')
    LArg = LArgParser.ArgParser.add_argument ('a2', type = str, default='^.*..*$', help = 'a2')
    LArg = LArgParser.ArgParser.add_argument ('a3', type = int, default=60, help = 'a3')
    # LArg = LArgParser.ArgParser.add_argument ('-a1', '--a1', type = str, default='', help = 'a1')
    # LArg = LArgParser.ArgParser.add_argument ('-a2', '--a2', type = str, default='^.*..*$', help = 'a2')
    # LArg = LArgParser.ArgParser.add_argument ('-a3', '--a3', type = int, default=60, help = 'a3')
    Largs = LArgParser.ArgParser.parse_args ()

    LA1 = Largs.a1
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, f'A1 = {LA1}')
    LA2 = Largs.a2
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, f'A2 = {LA2}')
    LA3 = Largs.a3
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, f'A3 = {LA3}')

    LULog.STOPLogging ()
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    # print(f'Вызов функции {__name__}')
    main()
#endif

#endmodule
