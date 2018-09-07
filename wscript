#!/usr/bin/python
# this is a smith configuration file

# set the version control system for srcdist
VCS = 'git'

# set the font name, version, licensing and description
APPNAME="Hispa"

DESC_SHORT = "Font for the Toto script"
DESC_LONG = """
The Hispa family of fonts supports the Toto script. This is currently
a work-in-progress, so these fonts and related files are preliminary
and incomplete. They should not be used for creating derivatives until
a later release.
"""
DESC_NAME = "Hispa"
BUILDLABEL = "alpha"

getufoinfo('source/masters/HispaMaster-Medium.ufo')

fontfamily=APPNAME
for dspace in ('Roman', ):
    designspace('source/' + fontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi")
    )
