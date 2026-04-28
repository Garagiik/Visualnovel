default path = ''
screen map:
    modal True
    zorder 101
    add 'map_bg' algin(.5,.5)
    imagebutton:
        xpos 1762 ypos 45
        idle 'exit'
        hover'exit_h'
        action Hide('map')
    if location == 'street':
        imagebutton:
        pos(339, 540)
        idle 'street_yes_i'
        hover 'street_yes'
        action NullAction()
    else:
        image
        # add (картинка карты в разработке)# align (.5,.5)

