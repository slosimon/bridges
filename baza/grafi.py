import matplotlib
import matplotlib.cbook
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from baza.models import Most, Dokumentacija_vsa
LIMIT = 14

def graph(request):
    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    # Get data from the database.
    most = Most.objects.all()
    leta=most.leto_rekonstrukcije_nov.all()
		let=leta.count()
		np=int(ceil(1 + log2(let)))
		hist(dogodki, np, normed=True, histtype='step');
		xlabel(r'Leto rekonstrukcije');
		ylabel(r'Število rekonstrukcij');
    # Create a png file and return it.
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
