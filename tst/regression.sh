# This runs the full suite of regression tests within the application.
# All test modules must be added here to ensure regression is performed via this script

nosetests -v tst.application_test &&
nosetests -v tst.entities.security_info_test &&
nosetests -v tst.util.calendar_util_test