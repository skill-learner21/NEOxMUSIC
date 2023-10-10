from DanishXmusic21.core.bot import Neox
from DanishXmusic21.core.dir import dirr
from DanishXmusic21.core.git import git
from DanishXmusic21.core.userbot import Userbot
from DanishXmusic21.misc import dbb, heroku

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
