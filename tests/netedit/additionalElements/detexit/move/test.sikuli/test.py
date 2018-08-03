#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot)

# apply zoom
netedit.setZoom("25", "0", "25")

# go to additional mode
netedit.additionalMode()

# select E3
netedit.changeAdditional("e3Detector")

# create E3
netedit.leftClick(match, 250, 50)

# select Exit detector
netedit.changeAdditional("detExit")

# Create Entry detector
netedit.leftClick(match, 250, 50)
netedit.leftClick(match, 100, 200)

# select Exit detector
netedit.changeAdditional("detEntry")

# Create Exit detector
netedit.leftClick(match, 250, 50)
netedit.leftClick(match, 100, 250)

# apply zoom out
netedit.setZoom("25", "0", "70")

# change to move mode
netedit.moveMode()

# move Entry to left
netedit.moveElement(match, 110, 200, 50, 200)

# move back
netedit.moveElement(match, 50, 200, 120, 200)

# move Entry to right
netedit.moveElement(match, 120, 200, 250, 200)

# move back
netedit.moveElement(match, 250, 200, 120, 200)

# move Entry to left overpassing lane
netedit.moveElement(match, 120, 200, -150, 200)

# move back
netedit.moveElement(match, -105, 200, 120, 200)

# move Entry to right overpassing lane
netedit.moveElement(match, 120, 200, 580, 200)

# move back to another different position of initial
netedit.moveElement(match, 550, 200, 300, 200)

# Check undos and redos
netedit.undo(match, 11)
netedit.redo(match, 11)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
