from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.nzb.binsearch.main import Base
from couchpotato.core.media.movie.providers.base import MovieProvider
from couchpotato.environment import Env

log = CPLog(__name__)


class BinSearch(MovieProvider, Base):

    def buildUrl(self, media, quality):
        query = tryUrlencode({
            'q': media['identifier'],
            'm': 'n',
            'max': 400,
            'adv_age': Env.setting('retention', 'nzb'),
            'adv_sort': 'date',
            'adv_col': 'on',
            'adv_nfo': 'on',
            'minsize': quality.get('size_min'),
            'maxsize': quality.get('size_max'),
        })
        return query