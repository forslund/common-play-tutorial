from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel

from mycroft.util.parse import match_one


track_dict = {
    'bomb jack': 'http://remix.kwed.org/files/RKOfiles/Chronblom%20-%20Bomb%20Jack%20subtune%206%20(violin%20version).mp3',
    'druid': 'http://remix.kwed.org/files/RKOfiles/Revel%20Craft%20-%20Druid.mp3',
    'crazy comets':  'http://remix.kwed.org/files/RKOfiles/Makke%20-%20Crazy%20Comets%20(Komet%20Non-Stop).mp3',
    'boulder dash': 'http://remix.kwed.org/files/RKOfiles/Mahoney%20-%20BoulderDash%20(Commodore%2069%20mix).mp3',
    'garfield': 'http://remix.kwed.org/files/RKOfiles/Reyn%20Ouwehand%20-%20Garfield.mp3'
}


class TutorialSkill(CommonPlaySkill):
    def CPS_match_query_phrase(self, phrase):
        """ This method responds wether the skill can play the input phrase.

            The method is invoked by the PlayBackControlSkill.

            Returns: tuple (matched phrase(str),
                            match level(CPSMatchLevel),
                            optional data(dict))
                     or None if no match was found.
        """
        # Get match and confidence
        match, confidence = match_one(phrase, track_dict)
        # If the confidence is high enough return a match
        if confidence > 0.5:
            return (match, CPSMatchLevel.TITLE, {"track": match})
        # Otherwise return None
        else:
            return None

    def CPS_start(self, phrase, data):
        """ Starts playback.

            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        url = data['track']
        self.audioservice.play(url)


def create_skill():
    return TutorialSkill()
