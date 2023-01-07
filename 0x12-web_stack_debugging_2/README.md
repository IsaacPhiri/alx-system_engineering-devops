# 0x12-web_stack_debugging_2

`100-fix_in_7_lines_or_less`
`This script is a simple shell script that makes a few changes to an Nginx server's configuration.

The first line chmod 644 /etc/nginx/nginx.conf sets the file permissions of the nginx.conf file to 644, making it readable and writable by the owner (usually root) and readable by others. This is a standard permissions setting for configuration files on a Linux system.

The next two lines both use the sed command to make changes to the nginx.conf file. Sed is a command-line text editor that can be used to perform basic text transformations on an input file. The -E flag tells sed to use extended regular expressions for pattern matching. The -i flag tells sed to edit the file in place, rather than outputting the result to standard output.
The first sed command sed -Ei 's/\s*#?\s*user .*/user nginx;/' /etc/nginx/nginx.conf matches any line in the file that starts with the word "user" followed by some whitespace and changes it to "user nginx;". This line is setting the user that Nginx process runs as.

The next sed command sed -Ei 's/(listen (\[::\]:)?80) /\180 /' /etc/nginx/sites-enabled/default matches any line containing the text "listen" and "80" and changes it to "listen 80". This line is changing the listening port of Nginx.

Next line pkill apache2 sends the TERM signal to the process group of all processes named apache2. This kills all running Apache2 processes.

The last line su nginx -s /bin/bash -c 'service nginx restart' runs the command 'service nginx restart' as the nginx user by switching the current user to 'nginx' and restart Nginx.`
`The command sed -Ei 's/\s*#?\s*user .*/user nginx;/' /etc/nginx/nginx.conf is using sed to make a change to the /etc/nginx/nginx.conf file. Specifically, it is searching for lines that start with the word "user" followed by some optional whitespace and an optional "#" (which indicates a comment), and replacing the entire line with "user nginx;".

Here is how the command works in detail:

s/: the 's' command tells sed to perform a search and replace operation
\s*#?\s*: this regular expression matches zero or more whitespace characters, followed by an optional "#" character, followed by zero or more whitespace characters. This pattern is matching the possible whitespaces or comments before the 'user' keyword.
user: matches the word "user"
.: matches any single character
*: matches zero or more of the preceding character
/user nginx;/: is the replacement string "user nginx;"
/: marks the end of the regular expression
/etc/nginx/nginx.conf: is the file to be edited`
