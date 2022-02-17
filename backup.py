import os
import sys
path = '/home/vlku1221/'
#print('Hello')
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])
#print(sys.argv[4])
x = len(sys.argv)
if x > 1:
    if sys.argv[1] == '--help':
        print("""\nmanage bases script\nallowed options and args:
--create_copy        base on the same server for tests
--show_backup        files in backup directory
--unpack_backup      file unpigz
--restore_base       from backup file to empty base
--show_db            show dabases 
--rename_db          rename database 
--delete_db          delete database
--create_empty       base for future restore from backup file
--create_backup      will create backup for choosen database 
--path /path/to/file
--show_backups""")
    #print('Arguments entered' + str(sys.argv[1:]))
else:
    print('args no provided\nPlease use:\n --help' )
if sys.argv == '--show_backups':
    files = os.listdir(path)
    print(files)
