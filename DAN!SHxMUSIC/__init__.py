from DAN!SHxMUSIC.core.bot import Neox
from DAN!SHxMUSIC.core.dir import dirr
from DAN!SHxMUSIC.core.git import git
from DAN!SHxMUSIC.core.userbot import Userbot
from DAN!SHxMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
