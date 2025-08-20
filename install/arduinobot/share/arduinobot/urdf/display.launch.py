from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    ld = LaunchDescription()

    pkg_path = FindPackageShare('arduinobot_description')
    default_model_path = PathJoinSubstitution([pkg_path, 'urdf', 'arduinobot.urdf.xacro'])
    default_rviz_config_path = PathJoinSubstitution([pkg_path, 'rviz', 'urdf.rviz'])

    gui_arg = DeclareLaunchArgument(
        name='gui', default_value='true', choices=['true', 'false'],
        description='Enable joint_state_publisher_gui'
    )
    rviz_arg = DeclareLaunchArgument(
        name='rvizconfig', default_value=default_rviz_config_path,
        description='Path to rviz config'
    )
    model_arg = DeclareLaunchArgument(
        name='model', default_value=default_model_path,
        description='URDF path'
    )

    ld.add_action(gui_arg)
    ld.add_action(rviz_arg)
    ld.add_action(model_arg)

    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([pkg_path, 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': 'arduinobot_description',
            'urdf_package_path': LaunchConfiguration('model'),
            'rviz_config': LaunchConfiguration('rvizconfig'),
            'jsp_gui': LaunchConfiguration('gui')
        }.items()
    ))

    return ld
