import math


class HohmannCalculator:
    def __init__(self, gravitational_constant: float = 6.67430e-11, orbital_body_mass: float = 5.97219e24):
        self.grav_c = gravitational_constant
        self.orbital_body_mass = orbital_body_mass

    def orbital_velocity(self, radius: float) -> float:
        """ 
            Calculate the velocity of an object in circular orbit around a given mass with 
            a given radius.    
        """
        return math.sqrt(
            (self.grav_c * self.orbital_body_mass)/radius
        )


    def post_burn_target_velocities(self, initial_radius: float, target_radius: float) -> tuple[float, float]:
        """
            Calculate the post-burn velocities required to achieve a transfer.
        """
        # Length of the Semi-major axis of the transfer orbit elliptical
        transferOrbitAxis = initial_radius + target_radius

        return (
            # Burn 1 target velocity
            math.sqrt(2 * self.grav_c * self.orbital_body_mass * ((1/initial_radius) - 1/(transferOrbitAxis))),
            # Burn 2 target velocity
            math.sqrt(2 * self.grav_c * self.orbital_body_mass * ((1/target_radius) - 1/(transferOrbitAxis)))
        )


    def calculate(self, initial_radius: float, target_radius: float) -> dict:
        # initial and final velocities based on the orbit radius
        initial_velocity = self.orbital_velocity(initial_radius)
        final_velocity = self.orbital_velocity(target_radius)
        # Post burn target velocities
        burn1_target, burn2_target = self.post_burn_target_velocities(initial_radius, target_radius)
        # Delta V 
        burn1_deltav = abs(initial_velocity - burn1_target)
        burn2_deltav = abs(final_velocity - burn2_target)

        return {
            "inital_velocity": initial_velocity,
            "burn1_target_velocity": burn1_target,
            "burn1_deltav": burn1_deltav,
            "burn2_target_velocity": burn2_target,
            "burn2_deltav": burn2_deltav,
            "final_velocity": final_velocity
        }






    


