from ..home import install


#
#   clients Client
#
from clients.models import Client

client_the_site = Client.objects.create(
    id=0,
    name='Education by survey',
    shortname='THE SITE',
    corporate=True,
    public=True,
)
