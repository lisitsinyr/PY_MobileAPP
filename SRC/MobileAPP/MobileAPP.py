"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     MobileAPP
     Python (PROJECTS_PY)
 Module:
     MobileAPP.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import time
import datetime

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import lyrpy.LULog as LULog
import lyrpy.LUParserARG as LUParserARG
import lyrpy.LUFile as LUFile
import lyrpy.LUProc as LUProc
import lyrpy.LUos as LUos
import lyrpy.LUDateTime as LUDateTime
import lyrpy.LUStrUtils as LUStrUtils

#------------------------------------------
# const
#------------------------------------------

#------------------------------------------
# RunProcessFile (aFileName: str, aPathWork: str)
#------------------------------------------
def RunProcessFile (aFileName: str, aPathWork: str):
#beginfunction
    # название электронной таблицы
    # Если в качестве значения указать список, то будет возвращён словарь датафреймов
    sheet_name = 0
    sheet_name = 'Лист1'
    # сколько строк вы хотите пропустить
    skiprows = None
    skiprows = 1
    # При установленном значении “0” используется первая строка.
    # Если у столбцов не должно быть заголовков, установите значение “None”
    header = 0
    header = 1
    # список с именами столбцов
    names = None
    # список с номерами или названиями столбцов.
    usecols = None
    #
    dtype = None
    nrows = None

    APPs = pandas.read_excel(aFileName, sheet_name = 'Лист1',skiprows = 1, header = 1,
                            names = None, usecols = None, dtype = None, nrows = None
                             )
    # print(APPs.index)
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, APPs.index)
    for row in APPs.itertuples():
        LFolderMobile = row[1]
        LLink = row[3]
        LType = row[4]
        LProgram = row[5]
        LShop = row[6]
        LFactory = row[7]
        LFolderPC = row[8]
        if LType == 'ПРОГРАММА' and LLink != '':
            sLFolderMobile = LUStrUtils.AddCharR ('.', LFolderMobile, 20)
            sLLink = LUStrUtils.AddCharR ('.', LLink, 50)
            sLFolderPC = LUStrUtils.AddCharR ('.', LFolderPC, 50)
            LULog.LoggerAPPS_AddLevel (LULog.TEXT, sLFolderMobile+sLLink+sLFolderPC)
            LFolderPCwork = aPathWork+'/'+LFolderMobile+'/'+LFolderPC
            if not LUFile.DirectoryExists (LFolderPCwork):
                # LUFile.ForceDirectories (LFolderPCwork)
                s = f'Директория: {LFolderPCwork}'
                LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
            #endif
        #endif
        if LType == 'ВИДЖЕТ':
            sLFolderMobile = LUStrUtils.AddCharR ('.', LFolderMobile, 20)
            sLLink = LUStrUtils.AddCharR ('.', LLink, 50)
            LULog.LoggerAPPS_AddLevel (LULog.TEXT, sLFolderMobile+sLLink)
        #endif
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI, 'console', 'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    LArgParser = LUParserARG.TArgParser (description = 'Параметры', prefix_chars = '-/')
    LArgFileName = LArgParser.ArgParser.add_argument ('FileName', type = str, default = '', help = 'FileName')
    LArgFileName.required = False
    LArgPathWork = LArgParser.ArgParser.add_argument ('PathWork', type = str, default = '', help = 'PathWork')
    LArgPathWork.required = False
    Largs = LArgParser.ArgParser.parse_args ()

    LFileName = Largs.FileName
    s = f'FileName = {LFileName}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT,s)

    LPathWork = Largs.PathWork
    s = f'PathWork = {LPathWork}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT,s)
    if LPathWork == '':
        LPathWork = LUos.GetCurrentDir()
    #endif

    if LUFile.FileExists(LFileName) & LUFile.DirectoryExists (LPathWork):
        RunProcessFile (LFileName, LPathWork)
        LResult = 0
    else:
        s = 'No such file or directory'
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
        LResult = 1
    #endif

    s = 'ExitProgram...'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    sys.exit(LResult)
#endfunction

#------------------------------------------
# MODULE
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
