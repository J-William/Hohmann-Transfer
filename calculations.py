import math

# Gravitational constant
gravC = 6.67430e-11


def orbital_velocity(massOfOrbitalBody, radius):
    """ 
        Calculate the velocity of an object in circular orbit around a given mass with 
        a given radius.    
    """
    return math.sqrt(
        (gravC * massOfOrbitalBody)/radius
    )


def post_burn_target_velocities(massOfOrbitalBody, initialRadius, targetRadius):
    """
        Calculate the post-burn velocities required to achieve a transfer.
    """
    # Length of the Semi-major axis of the transfer orbit elliptical
    transferOrbitAxis = initialRadius + targetRadius

    return (
        # Burn 1 target velocity
        math.sqrt(2 * gravC * massOfOrbitalBody * ((1/initialRadius) - 1/(transferOrbitAxis))),
        # Burn 2 target velocity
        math.sqrt(2 * gravC * massOfOrbitalBody * ((1/targetRadius) - 1/(transferOrbitAxis)))
    )


def burn_cal(massOfOrbitalBody, initialRadius, targetRadius):
    """
        Calculate the DeltaV values for both burns of a transfer
    """
    initV = orbital_velocity(massOfOrbitalBody, initialRadius)
    finV = orbital_velocity(massOfOrbitalBody, targetRadius)

    velo = post_burn_target_velocities(massOfOrbitalBody, initialRadius, targetRadius)

    return abs(initV - velo[0]), abs(finV - velo[1])



if __name__=="__main__":
    rad1 = 6_500_000
    rad2 = 13_000_000
    massOfEarth = 5.97219e24
    
    initialV = orbital_velocity(massOfEarth, rad1)
    targetV = orbital_velocity(massOfEarth, rad2)
    burn1Target, burn2Target = post_burn_target_velocities(massOfEarth, rad1, rad2)
    

    print(f"Initial Radius | Velocity: {'{:,}'.format(rad1)} | {initialV}")
    print(f"Target Radius | Velocity: {'{:,}'.format(rad2)} | {targetV}")
    print(f"Burn 1 target velocity: {burn1Target}")
    print(f"Burn 2 target velocity: {burn2Target}")
    print(f"Delta V for Burn 1: {abs(burn1Target - initialV)}")
    print(f"Delta V for Burn 2: {abs(burn2Target - targetV)}")


    


