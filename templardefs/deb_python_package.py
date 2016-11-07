'''
packging definitions
'''

def populate(d):
    # deb section
    d.deb_package=True
    d.deb_section='python'
    d.deb_priority='optional'
    d.deb_architecture='all'
    d.deb_pkgname='scrapers'
    # to which series to publish the package?
    d.deb_series=[
        'yakkety',
        'xenial',
        'wily',
        'vivid',
        # end of life
        #'utopic',
        'trusty',
        # does not accept new uploads
        #'saucy',
        # does not accept new uploads
        #'raring',
    ]
    d.deb_depends='${misc:Depends}, ${python3:Depends}, python3-mako'
    d.deb_builddepends='python3-all, python3-setuptools, python-all, python-setuptools, debhelper, dh-python'
    d.deb_standards_version='3.9.8'
    d.deb_x_python_version='>= 3.4'
    d.deb_x_python3_version='>= 3.4'
    d.deb_urgency='low'
    d.entry_points={
        'console_scripts': [
            'scape_fb_photos=scrape.scape_fb_photos:cli',
            'scape_tg_photos=scrape.scape_tg_photos:cli',
            'scape_ig_photos=scrape.scape_ig_photos:cli',
            'scape_vk_photos=scrape.scape_vk_photos:cli',
        ],
    }

def getdeps():
    return [
        __file__, # myself
    ]
