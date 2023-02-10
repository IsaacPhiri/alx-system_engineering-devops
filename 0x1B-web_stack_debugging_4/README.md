# 0x1B-web_stack_debugging_4

`0-the_sky_is_the_limit_not.pp` - This script will increase the ULIMIT of the default file, and restart Nginx. The require and notify parameters are used to ensure that the fix_for_nginx command runs before the nginx_restart command, and that nginx_restart runs after fix_for_nginx has completed.

`1-user_limit.pp` - In this script, two 'exec' resources are used to execute shell commands that modify the limits in the '/etc/security/limits.conf' file. The 'unless' attribute is used to prevent the resource from executing if the specified command returns a successful exit code. This is to ensure that the resources are only executed once and avoid multiple entries in the file.
