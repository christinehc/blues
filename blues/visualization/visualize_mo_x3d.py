from . import *
from choose_calculate_mo import *
from orbkit.display import init_display, display
import orbkit as ok



def mo_to_visualize(filename, before_homo, after_homo, selected_mo_string, 
                    contour1, contour2, notebook=True, 
                    opacity=0.3, scale_factor=0.5, wireframe=False,
                    saved_image='my_mo.png'):
                    
"""
x3d rendering can only be used in a Jupyter Notebook for now. If the user 
only wants a .png, change notebook=False

Parameters
---------
selected_mo_string: string of MO to plot 
    example: 'HOMO-3', 'LUMO', HOMO+5'
contour1: float < 1.0 for first isosurface
contour2: float < 1.0 for second isosurface    
    
Returns
---------
1 x3d or png rendering with 2 isosurfaces and atomic positions
"""

    if notebook = True:
        # clear figure and re-initialize notebook with x3d for interactive,
        # run this each time you want a new figure    
        mlab.clf()
        mlab.init_notebook('x3d',500,500)
    else:
        pass
        
    read_file, orbital_string_input = 
    my_mo_list(filename=filename, before_homo=before_homo, after_homo=after_homo)
    
    # convert string to index    
    selected_mo_string = selected_mo_string
    selected_mo = orbital_list.index(selected_mo_string)
    
    # contour spacing based on max density value
    contour1 = [mo_list[selected_mo].max()*contour1]
    contour2 = [mo_list[selected_mo].max()*contour2]
    
    opacity = 0.3
    # auto-set the image boundaries from grid previously set
    extent= [x.min(),x.max(),y.min(),y.max(),z.min(),z.max()]

    # build pipeline
    src = mlab.pipeline.scalar_field(mo_list[selected_mo])
    
    isosurf = mlab.pipeline.iso_surface(
        src, contours=contour1, opacity=opacity, 
        color=(0, 0, 0.8), extent=extent)
    # second isosurface
    isosurf = mlab.pipeline.iso_surface(
        src, contours=contour2, opacity=opacity, 
        color=(0.8, 0, 0), extent=extent)
    
    # plot atomic positions
    # make oxygens red
    isosurf = mlab.points3d(xo, yo, zo, color=(1.0,0.0,0.0), scale_factor=scale_factor)
    # make nitrogen blue
    isosurf = mlab.points3d(xn, yn, zn, color=(0.0,0.0,1.0), scale_factor=scale_factor)
    # all others (should be mostly carbon), white
    isosurf = mlab.points3d(xc, yc, zc, scale_factor=scale_factor)
        
    if wireframe=True:
        iso.actor.property.representation = 'wireframe'
    else:
        pass
    
        if notebook=False:
        mlab.axes()
        mlab.options.offscreen = True
        mlab.savefig(figure=fig, filename=saved_image)
    else:
        pass
        
    return 