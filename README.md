# nagios-agents-metadata

This is a collection of files containing OCF metadata for the
respective nagios monitoring agents for use with Pacemaker.

The metadata was initially extracted from the help pages of
monitoring agents living in
https://github.com/monitoring-plugins/monitoring-plugins
version 1.4.16 (on Feb 5 2013).

In order to use these files, it is necessary to add
--with-nagios=true to the configure invocation before compiling
Pacemaker.

There is no configuration and the installation is very simple.
Please see the sample spec file.

Nagios metadata is part of the SUSE SLEHA product. The relevant
documentation is available here:

https://www.suse.com/documentation/sle_ha/singlehtml/book_sleha/book_sleha.html#sec.ha.configuration.basics.nagios

Integration with upstream
=========================

It would be possible to produce the metadata directly from the
nagios plugins. One implementation is available at
https://github.com/dmuhamedagic/nagios-plugins/tree/metadata
(see the last 4 commits).


