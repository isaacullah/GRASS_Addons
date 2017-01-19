#!/usr/bin/python
#
############################################################################
#
# MODULE:       	r.commons.py
# AUTHOR(S):		Isaac Ullah, Arizona State University
# PURPOSE:		Define the areas that can be considered "the commons" for analysis of the "Tragedy of the Commons" in an area with multiple sites. Module requires r.walk.
# ACKNOWLEDGEMENTS:	National Science Foundation Grant #BCS0410269 
# COPYRIGHT:		(C) 2009 by Isaac Ullah, Michael Barton, Arizona State University
#			This program is free software under the GNU General Public
#			License (>=v2). Read the file COPYING that comes with GRASS
#			for details.
#
#############################################################################


#%Module
#%  description: Define the areas that can be considered "the commons" for analysis of the "Tragedy of the Commons" in an area with multiple sites using the "commons equation". Module requires r.walk.
#%END

#%option
#% key: elev
#% type: string
#% gisprompt: old,cell,raster
#% description: Input elevation map (DEM)
#% required : yes
#%END

#%option
#% key: vect
#% type: string
#% gisprompt: old,vector,vector
#% description: Name of input vector points map containg the set of sites for this analysi.
#% required : yes
#%END

#%option
#% key: x_column
#% type: string
#% description: Column containing x values for site coordinates
#% required : yes
#%END

#%option
#% key: y_column
#% type: string
#% description: Column containing y values for site coordinates
#% required : yes
#%END

#%option
#% key: i_column
#% type: string
#% description: Column containing values of i ("importance index") for each site in input vector map
#% required : yes
#%END

#%option
#% key: name_column
#% type: string
#% description: Column with unique identifiers for each site in input vector map (CAT column can be used)
#% required : yes
#%END

#%option
#% key: cvmax
#% type: string
#% description: Cost surface value (seconds of walking time) encompassing the zone of 100% usage for the largest/most important site in site set.
#% required : yes
#%END

#%option
#% key: frict
#% type: string
#% gisprompt: old,cell,raster
#% description: Optional map of extra "friction" costs. If no map selected, "friction" = 1
#% answer:
#% required : no
#%END

#%flag
#% key: k
#% description: -k Use knight's move for calculating cost surface (slower but more accurate)
#%END
#%flag
#% key: c
#% description: -c Keep all the interim cost surface used to calculate the commons equation
#%END


import sys
import os
import subprocess
import tempfile
import random
grass_install_tree = os.getenv('GISBASE')
sys.path.append(grass_install_tree + os.sep + 'etc' + os.sep + 'python')
import grass.script as grass


#main block of code starts here
def main():
    #bring in input variables
    elev = os.getenv("GIS_OPT_elev")
    vect = os.getenv("GIS_OPT_vect")
    xcol = os.getenv("GIS_OPT_cfact_x_column")
    ycol = os.getenv("GIS_OPT_y_column")
    icol = os.getenv("GIS_OPT_i_column")
    namecol = os.getenv("GIS_OPT_name_column")
    
    #read in info from the table of the vector sites map, and parse it into a list of lists of info for each site
    s1 = grass.read_command("v.db.select", quiet = "True", map = vect, columns = xcol + "," + ycol + "," + icol + "," + namecol, fs = ",", nv = "False").strip()
    masterlist = []
    for item in s1.split("\n"):
        masterlist.append(item.strip("\n").split(","))
    #the first row is the column names, so pop that out of our master list
    indexlist = masterlist.pop(0)
    #now, loop through the master list and run r.walk for each of the sites, and append the cost surfaces to a list (so we can work with them later)
    for site in masterlist:
        #DO SOME CODE ### STILL TO DO ###

# here is where the code in "main" actually gets executed. This way of programming is neccessary for the way g.parser needs to run.
if __name__ == "__main__":
    if ( len(sys.argv) <= 1 or sys.argv[1] != "@ARGS_PARSED@" ):
        os.execvp("g.parser", [sys.argv[0]] + sys.argv)
    else:
        main()
