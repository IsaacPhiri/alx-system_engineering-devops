# 0x1B-web_stack_debugging_4

`0-the_sky_is_the_limit_not.pp` - This script will increase the ULIMIT of the default file, and restart Nginx. The require and notify parameters are used to ensure that the fix_for_nginx command runs before the nginx_restart command, and that nginx_restart runs after fix_for_nginx has completed.


