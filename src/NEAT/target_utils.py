import jax.numpy as jnp

def get_distance_to_closest_target(disk_position, targets):
    """Calculate distance to closest target."""
    distances = jnp.array([
        jnp.linalg.norm(disk_position - targets[0][:2]),
        jnp.linalg.norm(disk_position - targets[1][:2])
    ])
    return jnp.min(distances), jnp.argmin(distances)

def get_direction_to_closest_target(disk_position, disk_rotation, target):
    """Calculate direction to the single target relative to disk orientation."""
    target_position = target[:2]
    direction_vector = target_position - disk_position
    
    distance = jnp.linalg.norm(direction_vector)
    unit_direction = direction_vector / jnp.where(distance > 0, distance, 1.0)
    
    target_angle = jnp.arctan2(unit_direction[1], unit_direction[0])
    
    # Calculate angle difference (between -pi and pi)
    # This gives relative angle between disk orientation and target
    angle_diff = jnp.mod(target_angle - disk_rotation + jnp.pi, 2 * jnp.pi) - jnp.pi
    
    return jnp.array([angle_diff])
