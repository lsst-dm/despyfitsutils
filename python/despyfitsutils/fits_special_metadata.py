#!/usr/bin/env python
"""Specialized functions for computing metadata.
"""

from astropy.io import fits
import despyfitsutils.fitsutils as fitsutils
import despymisc.create_special_metadata as spmeta


######################################################################
# !!!! Function name must be all lowercase
# !!!! Function name must be of pattern func_<header key>
######################################################################


def func_band(filename, hdulist=None, whichhdu=None):
    """Create band from the filter keyword.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    filterval = fitsutils.get_hdr_value(hdulist2, 'FILTER', whichhdu)

    if hdulist is None:
        hdulist2.close()

    return spmeta.create_band(filterval)


def func_camsym(filename, hdulist=None, whichhdu=None):
    """Create camsys from the INSTRUME keyword.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    instrume = fitsutils.get_hdr_value(hdulist2, 'INSTRUME', whichhdu)

    if hdulist is None:
        hdulist2.close()

    return spmeta.create_camsym(instrume)


def func_nite(filename, hdulist=None, whichhdu=None):
    """Create nite from the DATE-OBS keyword.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    date_obs = fitsutils.get_hdr_value(hdulist2, 'DATE-OBS', whichhdu)

    if hdulist is None:
        hdulist2.close()

    return spmeta.create_nite(date_obs)


def func_objects(filename, hdulist=None, whichhdu=None):
    """Return the number of objects in fits catalog.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    objects = fitsutils.get_hdr_value(hdulist2, 'NAXIS2', whichhdu)

    if hdulist is None:
        hdulist2.close()

    return objects


def func_field(filename, hdulist=None, whichhdu=None):
    """Return the field from OBJECT fits header value.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    try:
        objectval = fitsutils.get_hdr_value(hdulist2, 'OBJECT', whichhdu)
    except:
        objectval = fitsutils.get_hdr_value(hdulist2, 'OBJECT', 'LDAC_IMHEAD')

    if hdulist is None:
        hdulist2.close()

    return spmeta.create_field(objectval)


def func_radeg(filename, hdulist=None, whichhdu=None):
    """Return the fits header value RA in degrees.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    ra = fitsutils.get_hdr_value(hdulist2, 'RA', whichhdu)

    if hdulist is None:
        hdulist2.close()

    return spmeta.convert_ra_to_deg(ra)


def func_tradeg(filename, hdulist=None, whichhdu=None):
    """Return the fits header value TELRA in degrees.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    telra = fitsutils.get_hdr_value(hdulist2, 'TELRA')

    if hdulist is None:
        hdulist2.close()

    return spmeta.convert_ra_to_deg(telra)


def func_decdeg(filename, hdulist=None, whichhdu=None):
    """Return the fits header value DEC in degrees.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    dec = fitsutils.get_hdr_value(hdulist2, 'DEC', whichhdu)

    if hdulist is None:
        hdulist2.close()

    return spmeta.convert_dec_to_deg(dec)


def func_tdecdeg(filename, hdulist=None, whichhdu=None):
    """Return the fits header value TELDEC in degrees.
    """
    hdulist2 = None
    if hdulist is None:
        hdulist2 = fits.open(filename, 'readonly')
    else:
        hdulist2 = hdulist

    teldec = fitsutils.get_hdr_value(hdulist2, 'TELDEC')

    if hdulist is None:
        hdulist2.close()

    return spmeta.convert_dec_to_deg(teldec)
