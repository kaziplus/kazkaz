"""

"""
def filter_seekers(seekers, profile):
    """filter out seekers based on Profile

    """
    seekers = rank_seekers(seekers, profile)

    return seekers[:10]


def rank_seekers(seekers, profile):
    """rank seekers

    """
    scores = [{'seeker': seeker, 'score': seeker.compute_score(profile)}
              for seeker in seekers]

    scores.sort(key=lambda x: x['score'], reverse=True)
    print(scores)

    seekers = [score['seeker'] for score in scores]

    return seekers


# ============================================================================
# EOF
# ============================================================================
