#! python
# SImulate Brush#

# 1. Select object
# 2. Run Script
# 	1. Get selected object.
# 	2. Create rigid body ex and copy model to rigidbodyex
# 	3. snap rigid body ex to xform of selected object
# 	4. and prompt user for weight
# 	5. hide selected object
# 	6. simulate rigidbody ex
# 	7. after simulation is done copy original object to new xform of simulated rigid body
# 	8. delete rigid body.
import general
import lodtools
import physics

from user_values import UserValues

PHYS_OBJECT_NAME = "brush_sim_temp"


if __name__ == "__main__":
    store = UserValues()
    stored_brush = store.get("simmed_brush")
    # 	1. Get selected object.
    # grab some properties for our selected object
    user_selection = general.get_names_of_selected_objects()[0]

    if stored_brush is None:
        print('Simulating Brush')
        # store the users selection for setting the physics state later on
        store.set("simmed_brush", user_selection)
        # grab the transforms of the object
        obj_pos = general.get_position(user_selection)
        obj_rot = general.get_rotation(user_selection)
        obj_scale = general.get_scale(user_selection)

        # 	2. Create rigid body ex and copy model to rigidbodyex
        # create the object at 0,0,0
        PHYS_OBJECT_NAME = general.new_object(
            "Entity", r"RigidBodyEx", PHYS_OBJECT_NAME, 0, 0, 0
        )
        # mark it with a special material so you know it's being simulated
        general.set_custom_material(PHYS_OBJECT_NAME, 'Materials/Special/green_screen.mtl')
        # set the physobj to be the selected brush object
        user_selection_brush = str(lodtools.getselected())
        general.set_entity_geometry_file(PHYS_OBJECT_NAME, user_selection_brush)

        # 	3. snap physobj to xform of selected object
        general.set_position(
            PHYS_OBJECT_NAME, int(obj_pos[0]), int(obj_pos[1]), int(obj_pos[2])
        )
        general.set_rotation(
            PHYS_OBJECT_NAME, int(obj_rot[0]), int(obj_rot[1]), int(obj_rot[2])
        )
        general.set_scale(
            PHYS_OBJECT_NAME, int(obj_scale[0]), int(obj_scale[1]), int(obj_scale[2])
        )

        # 5 Hide user selection object
        general.log("hiding " + user_selection)
        general.hide_object(user_selection)

        # 	6. simulate physobj
        # select the physics object
        general.select_object(PHYS_OBJECT_NAME)
        # simulate it
        physics.simulate_selection()

    else:
        print('Converting Physics Object to Brush')
        # get the state of the physics objects
        physics.get_state(PHYS_OBJECT_NAME)
        # get the transforms of the simulated physics object
        phys_pos = general.get_position(PHYS_OBJECT_NAME)
        phys_rot = general.get_rotation(PHYS_OBJECT_NAME)
        phys_scale = general.get_scale(PHYS_OBJECT_NAME)
        # unhide the original object
        general.unhide_object(user_selection)
        # set the transforms of the original object to have the transforms of the simulated object
        general.set_position(user_selection, phys_pos[0], phys_pos[1], phys_pos[2])
        general.set_rotation(user_selection, phys_rot[0], phys_rot[1], phys_rot[2])
        general.set_scale(user_selection, phys_scale[0], phys_scale[1], phys_scale[2])
        # delete the physics object
        general.clear_selection()
        general.delete_object(PHYS_OBJECT_NAME)
        # reselect the users original selection
        general.select_object(user_selection)
        # delete the simmed brush key so we can simulate another model
        store.delete("simmed_brush")
