    # Functions for basic fight actions

def seme(intensity, target, fighter = ""):

    """Set fighter's seme to prepare uchi

    Keyword arguments:
    intensity -- Take value from 1 to 5 to define threat and readability level
    target -- Take value Men, Kote, Do, Tsuki to define target
    fighter -- Set the fighter initiating the seme (feature in anticipation of a 2-player mode)
    """

    fighter_seme_intensity = intensity
    fighter_seme_target = target