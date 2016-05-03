=======
Preface
=======

This document lists the functions, constant, macros, feature flags,
and types defined in the POSIX 1003.1 standard.  Each section in
this document corresponds to a section in the 1003.1 standard
and the implementation status of the items required by the standard
are listed.

RTEMS supports a number of POSIX process, user, and group oriented
routines in what is referred to as a "SUSP" (Single-User, Single
Process) manner.  RTEMS supports a single process, multithreaded
POSIX 1003.1b environment.  In a pure world, there would be
no reason to even include routines like ``getpid()`` when there
can only be one process.  But providing routines like ``getpid()``
and making them work in a sensible fashion for an embedded environment
while not returning ENOSYS (for not implemented) makes it significantly
easier to port code from a UNIX environment without modifying it.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

