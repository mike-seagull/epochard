"""
convert epoch to date time
"""
import os.path
import os
import time
import sys
import re

def usage():
    print("usage: %s [FILE|DIRECTORY]" % os.path.basename(sys.argv[0]))
    print("%s: error: a FILE or a DIRECTORY is required" % (os.path.basename(sys.argv[0])))

def get_backups(backup_dir):
    """ This returns only the names of files and dirs in the given dir
    This does not give the full path
    """
    return os.listdir(backup_dir)

def get_all_dates_from_list_of_backup_strings(regex, list_of_backups, backup_dir="./"):
    dates = {}
    pattern = re.compile(regex)
    for backup in list_of_backups:
        for match in [pattern.search(backup)]:
            if match:
                # this is {date_string: {filename: "", path: ""}}
                epoch = int(match.group(0))
                date = time.strftime('%Y-%m-%d', time.localtime(epoch)) # convert epoch to date
                dates[date] = {
                    "filename": backup,
                    "path": os.path.join(backup_dir, backup)
                }
    return dates

def main(arg):
    if arg.isdigit():
        epoch = int(arg)
        date = time.strftime('%Y-%m-%d', time.localtime(epoch))
        print("%s\t%s" % (arg, date))
    else:
        if os.path.isdir(arg):
            backups = get_backups(arg)
        else:
            backups = [arg]
        dates = get_all_dates_from_list_of_backup_strings(r'(?<=config\.)(\d+)(?=\.xml)', backups)
        for date in dates:
            print("%s\t%s" % (os.path.basename(dates[date]['filename']), date))
    

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
        if arg:
            main(arg)
        else:
            usage()
    except IndexError as ie:
        usage()
