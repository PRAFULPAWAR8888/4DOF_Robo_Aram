from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    urdf_tutorial_path = FindPackageShare('urdf_tutorial')

    default_model_path = PathJoinSubstitution([
        FindPackageShare('arduinobot_description'),
        'urdf',
        'arduinobot.urdf.xacro'
    ])

    default_rviz_config_path = PathJoinSubstitution([
        urdf_tutorial_path, 'rviz', 'urdf.rviz'
    ])

    gui_arg = DeclareLaunchArgument(
        name='gui',
        default_value='true',
        choices=['true', 'false'],
        description='Flag to enable joint_state_publisher_gui'
    )

    rviz_arg = DeclareLaunchArgument(
        name='rvizconfig',
        default_value=default_rviz_config_path,
        description='Absolute path to rviz config file'
    )

    model_arg = DeclareLaunchArgument(
        name='model',
        default_value=default_model_path,
        description='Path to robot urdf/xacro file'
    )

    return LaunchDescription([
        gui_arg,
        rviz_arg,
        model_arg,
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('urdf_launch'),
                    'launch',
                    'display.launch.py'
                ])
            ]),
            launch_arguments={
                'urdf_package': 'arduinobot_description',
                'urdf_package_path': LaunchConfiguration('model'),  # ✅ pass the file path, not xacro output
                'rviz_config': LaunchConfiguration('rvizconfig'),
                'jsp_gui': LaunchConfiguration('gui')
            }.items()
        )
    ])
