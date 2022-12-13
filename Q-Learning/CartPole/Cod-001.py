import numpy as np




def build_state(features):
    return int("".join(map(lambda feature: str(int(feature)), features)))

def to_bin(value, bins):
    return np.digitize(x=[value], bins=bins)



print(np.digitize(x=[15], bins=np.linspace(-3.5, 3.5, 9)))
print (np.linspace(-3.5, 3.5, 9))

class FeatureTransformer:
    def __init__(self) -> None:
        self.cartPositionBins = np.linspace(-2.4, 2.4, 9)
        self.cartVelocityBins = np.linspace(-2, 2, 9)
        self.poleAngleBins = np.linspace(-0.4, 0.4, 9)
        self.poleVelocityBins = np.linspace(-3.5, 3.5, 9)

    def transform(self, observation):
        cartPos, cartVel, poleAngle, poleVel = observation
        return build_state(to_bin(cartPos, self.cartPositionBins),
                           to_bin(cartVel, self.cartVelocityBins),
                           to_bin(poleAngle, self.poleAngleBins),
                           to_bin(poleVel, self.poleVelocityBins))

