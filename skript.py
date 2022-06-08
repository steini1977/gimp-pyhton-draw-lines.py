#!/usr/bin/env python
#designed in windows10 notepad plus plus.
from gimpfu import *
def python-ribon-flow(image, drawable):
    # function code goes here..
    #
    #stop undo recording
    pdb.gimp_image_undo_group_start(image)
    #
    # brush/pencil size 
    size = 2
    pdb.gimp_context_set_brush_size(size)
    #
    # top color-ribon
    # counting up
    for n in range(0,image.width,size):
      #
      # gets a color-sample       True if sample all layers, True if avrage of colors is set, size is the avrage radius
      color = pdb.gimp_image_pick_color(image, drawable, n, 202, False, False, size)
      #
      # set the color-sample
      pdb.gimp_context_set_foreground(color)
      #
      # num_stroke is the stroke data-nubers (alway in pair x and y)
      num_strokes = 4
      #
      # sets the line pointers
      strokes = [n,0,n,200]
      #
      # executes the line-draw function
      pdb.gimp_pencil(drawable, num_strokes, strokes)
    #
    # bottom color-ribon
    for n in range(0,image.width,size):
      color = pdb.gimp_image_pick_color(image, drawable, n,image.height-202, False, False, size)
      pdb.gimp_context_set_foreground(color)
      num_strokes = 4
      strokes = [n,image.height-200,n,image.height]
      pdb.gimp_pencil(drawable, num_strokes, strokes)
    #
    # starts to record undo
    pdb.gimp_image_undo_group_end(image)
#end of script
register(
    "python-ribon-flow",
    "mix colors and adds ribbon stripes",
    "splash",
    "Stein-Ove Bratthammer", "Stein-Ove Bratthammer", "2022",
    "add ribbon to photo",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    python_ribon_flow, menu="<Image>/My")  # second item is menu location

main()
