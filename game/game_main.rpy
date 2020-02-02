################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Main
################################################################################
screen game_buttonControll(xoffset_max):

    zorder 200

    if not renpy.get_screen('game_map_street_1'):

        text _(str(xoffset_max*-1)) xpos 200 ypos 100 color '#000'
        text _(str(global_xoffset)) xpos 200 ypos 200 color '#000'

        imagebutton:
            keysym 'z'
            xalign 0.95 yalign 0.2
            auto 'sarr_%s'
            # if abs(global_xoffset-10) > abs(xoffset_max):
            #     action NullAction()
            # elif abs(global_xoffset-10) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
            #     action SetVariable('global_xoffset', xoffset_max*-1)
            # else:
            action [SetVariable('global_xoffset', global_xoffset-20),
                    Hide('chaMoveCon'),
                    Show('chaMoveCon', cha='m_walk_slow_sing')]

        imagebutton:
            keysym 'x'
            xalign 0.95 yalign 0.5
            auto 'farr_%s'
            # if abs(global_xoffset-150) > abs(xoffset_max):
            #     action NullAction()
            # elif abs(global_xoffset-150) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
            #     action SetVariable('global_xoffset', xoffset_max*-1)
            # else:
            action [SetVariable('global_xoffset', global_xoffset-90),
                    Hide('chaMoveCon'),
                    Show('chaMoveCon', cha='m_walk_fast_sing')]

        imagebutton:
            keysym 'K_SPACE'
            xalign 0.95 yalign 0.8
            auto 'inter_%s'
            action SetVariable('interact', interact+1)