
import os.path

from django.utils.functional import lazy
from django.utils.translation import ugettext as _
from django.conf import settings


def setting(name, editable=False, default=None):
    """
    Settings that can be edited via the admin. Uses Django's ``lazy`` util 
    to allow setting to be lazily loaded from the ``Setting`` model. 
    """
    value = getattr(settings, "MEZZANINE_%s" % name, default)
    setting_type = type(default)
    if editable:
        def query():
            from mezzanine.settings.models import Setting
            try:
                setting_obj = Setting.objects.get(name=name)
            except Setting.DoesNotExist:
                return default
            return setting_type(setting_obj.value)
        value = lazy(query, setting_type)()
    globals()[name] = value
    

# Unregister these models installed by default (occurs in urlconf).
setting("ADMIN_REMOVAL", default=())

# Controls the ordering and grouping of the admin menu.
setting("ADMIN_MENU_ORDER", default=(
    (_("Content"), ("pages.Page", "blog.BlogPost", "blog.Comment",)),
    (_("Site"), ("auth.User", "auth.Group", "sites.Site", 
        "redirects.Redirect")),
))

# Credentials for bit.ly URL shortening service.
setting("BLOG_BITLY_USER", editable=True, default="")
setting("BLOG_BITLY_KEY", editable=True, default="")

# Number of blog posts to show on a blog listing page.
setting("BLOG_POST_PER_PAGE", editable=True, default=5)

# Maximum number of paging links to show on a blog listing page.
setting("BLOG_POST_MAX_PAGING_LINKS", editable=True, default=10)

# Slug of the page object for the blog.
setting("BLOG_SLUG", default="blog")

# Shortname when using the Disqus comments system (http://disqus.com).
setting("COMMENTS_DISQUS_SHORTNAME", editable=True, default="")

# Disqus user's API key for displaying recent comments in the admin dashboard.
setting("COMMENTS_DISQUS_KEY", editable=True, default="")

# If True, the built-in comments are approved by default.
setting("COMMENTS_DEFAULT_APPROVED", editable=True, default=True)

# Number of latest comments to show in the admin dashboard.
setting("COMMENTS_NUM_LATEST", editable=True, default=5)

# If True, unapproved comments will have a placeholder visible on the site
# with a "waiting for approval" or "comment removed" message based on the
# workflow around the ``MEZZANINE_COMMENTS_DEFAULT_APPROVED`` setting - if
# True then the former message is used, if False then the latter.
setting("COMMENTS_UNAPPROVED_VISIBLE", editable=True, default=True)

# Media files for admin.
CONTENT_MEDIA_PATH = os.path.join(os.path.dirname(__file__), "core", "media")

# URL for serving internal media files.
setting("CONTENT_MEDIA_URL", default="/content_media/")

# Content status choices.
CONTENT_STATUS_DRAFT = 1
CONTENT_STATUS_PUBLISHED = 2
CONTENT_STATUS_CHOICES = (
    (CONTENT_STATUS_DRAFT, _("Draft")),
    (CONTENT_STATUS_PUBLISHED, _("Published")),
)

# A sequence of three sequences that make up the template tags used to render 
# the admin dashboard.
setting("DASHBOARD_TAGS", default=(
    ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
    ("blog_tags.recent_comments",),
    ("mezzanine_tags.recent_actions",),
))

# Maximum allowed length for field values in the forms app.
setting("FORMS_FIELD_MAX_LENGTH", default=2000)

# Maximum allowed length for field labels in the forms app.
setting("FORMS_LABEL_MAX_LENGTH", default=200)

# Absolute path where files will be uploaded to for the forms app.
setting("FORMS_UPLOAD_ROOT", default="")

# ID for using Google Analytics (http://www.google.com/analytics/) referred to
# as "Web Property ID".
setting("GOOGLE_ANALYTICS_ID", editable=True, default="")

# Strings to check for in user agents when testing for a mobile device.
setting("MOBILE_USER_AGENTS", editable=False, default=(
    "2.0 MMP", "240x320", "400X240", "AvantGo",
    "BlackBerry", "Blazer", "Cellphone", "Danger", "DoCoMo", "Elaine/3.0",
    "EudoraWeb", "Googlebot-Mobile", "hiptop", "IEMobile", "KYOCERA/WX310K",
    "LG/U990", "MIDP-2.", "MMEF20", "MOT-V", "NetFront", "Newt", "Nintendo Wii",
    "Nitro", "Nokia", "Opera Mini", "Palm", "PlayStation Portable", "portalmmm",
    "Proxinet", "ProxiNet", "SHARP-TQ-GX10", "SHG-i900", "Small",
    "SonyEricsson", "Symbian OS", "SymbianOS", "TS21i-10", "UP.Browser",
    "UP.Link", "webOS", "Windows CE", "WinWAP", "YahooSeeker/M1A1-R2D2",
    "iPhone", "iPod", "Android", "BlackBerry9530", "LG-TU915 Obigo", "LGE VX",
    "webOS", "Nokia5800"))

# Number of different sizes given to tags when shown as a cloud.
setting("TAG_CLOUD_SIZES", editable=True, default=4)

# If True, the pages menu will show all levels of navigation by default,
# otherwise child pages are only shown when viewing the parent page.
setting("PAGES_MENU_SHOW_ALL", default=True)

# Number of results to show in the search results page.
setting("SEARCH_PER_PAGE", editable=True, default=10)

# Maximum number of paging links to show in the search results page.
setting("SEARCH_MAX_PAGING_LINKS", editable=True, default=10)

# List of words which will be stripped from search queries.
setting("STOP_WORDS", default=(
    "a", "about", "above", "above", "across", "after",
    "afterwards", "again", "against", "all", "almost", "alone", "along",
    "already", "also", "although", "always", "am", "among", "amongst",
    "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone",
    "anything", "anyway", "anywhere", "are", "around", "as", "at", "back",
    "be", "became", "because", "become", "becomes", "becoming", "been",
    "before", "beforehand", "behind", "being", "below", "beside", "besides",
    "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can",
    "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe",
    "detail", "do", "done", "down", "due", "during", "each", "eg", "eight",
    "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even",
    "ever", "every", "everyone", "everything", "everywhere", "except", "few",
    "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former",
    "formerly", "forty", "found", "four", "from", "front", "full", "further",
    "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her",
    "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself",
    "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in",
    "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep",
    "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may",
    "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most",
    "mostly", "move", "much", "must", "my", "myself", "name", "namely",
    "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none",
    "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often",
    "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise",
    "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
    "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming",
    "seems", "serious", "several", "she", "should", "show", "side", "since",
    "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something",
    "sometime", "sometimes", "somewhere", "still", "such", "system", "take",
    "ten", "than", "that", "the", "their", "them", "themselves", "then",
    "thence", "there", "thereafter", "thereby", "therefore", "therein",
    "thereupon", "these", "they", "thickv", "thin", "third", "this", "those",
    "though", "three", "through", "throughout", "thru", "thus", "to",
    "together", "too", "top", "toward", "towards", "twelve", "twenty", "two",
    "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we",
    "well", "were", "what", "whatever", "when", "whence", "whenever", "where",
    "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever",
    "whether", "which", "while", "whither", "who", "whoever", "whole", "whom",
    "whose", "why", "will", "with", "within", "without", "would", "yet", "you",
    "your", "yours", "yourself", "yourselves", "the"))

setting("TINYMCE_URL", default="%s/tinymce" % settings.ADMIN_MEDIA_PREFIX)