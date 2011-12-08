#!/bin/bash
# 2011-12-08 Aurelio Jargas, MIT license
#
# Convert files from ISO-8859-1 to UTF-8 encoding,
# keeping the modification time (mtime) unchanged.
#
# With no command line arguments, only shows information.
# Use any argument to run this script for real, converting files.
# The original file is saved with the .iso2utf extension as a backup.
#
# DRY RUN (no conversion):
#   file --mime-encoding *.txt | grep iso-8859-1 | ./iso2utf-mtime.sh
#
# REAL RUN (perform conversion):
#   file --mime-encoding *.txt | grep iso-8859-1 | ./iso2utf-mtime.sh go
#
#
##### Tested in Mac OS X 10.7.2
#
### COMPATIBILITY:
#
# Usage of 'touch' command:
#
#   touch ... -t [[CC]YY]MMDDhhmm[.SS] file
#
# Sample 'stat' command output:
#
#   $ stat -t %Y%m%d%H%M.%S /etc/passwd
#   234881026 14380 -rw-r--r-- 1 root wheel 0 5148 "201112081210.06" "201110192237.32" "201110192237.32" "201108162241.05" 4096 0 0x20 /etc/passwd
#
#
# ***** If yours is any different, you'll have to adapt this script. *****
# ***** If yours is any different, you'll have to adapt this script. *****
# ***** If yours is any different, you'll have to adapt this script. *****
#


tmp=/tmp/iso2utf

# No command line parameters == DRY RUN
dryrun=1; [ "$1" ] && dryrun=0


# The file list comes from STDIN, one per line
while read file
do
	# Save the original file current mtime
	mtime=$(stat -t %Y%m%d%H%M.%S "$file" | cut -d ' ' -f 10 | tr -d \")

	if test $dryrun -eq 1
	then
		# Just show the touch command, with mtime expanded
		echo touch -t "$mtime" "$file"
	else
		# Save a backup, just in case
		cp -a "$file" "$file.iso2utf"

		# Perform the conversion
		iconv -f iso-8859-1 -t utf-8 "$file" > "$tmp"
		cat "$tmp" > "$file"  # Don't use 'mv' to preserve attributes

		# Restore original mtime
		touch -t "$mtime" "$file"

		echo "Done: $file"
	fi
done

### Conversion done

if test $dryrun -eq 0
then
	echo
	echo "To remove the backup files run this command:"
	echo 'find . -name "*.iso2utf" -exec rm {} \;'

	rm "$tmp"
fi

