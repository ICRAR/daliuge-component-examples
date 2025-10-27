#
#    ICRAR - International Centre for Radio Astronomy Research
#    (c) UWA - The University of Western Australia, 2017
#    Copyright by UWA (in the framework of the ICRAR)
#    All rights reserved
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston,
#    MA 02111-1307  USA
#

# A trivial example
import gzip
import shutil
import numpy as np


def output(arg: str, kw: str = "Universe") -> str:
    """
    Simple function formatting a Hello World output.

    Parameters:
    -----------
    arg: str, the word after Hello
    kw: str, the word after and

    Returns:
    --------
    str, 'Hello _arg_ and _kw_' message
    """
    return f"Hello {arg} and {kw}"


def create_array(size: int) -> np.array:
    """
    Simple array generation using numpy.

    Parameters:
    -----------
    size: int, the size of the array

    Returns:
    --------
    np.array, a numpy array of _size_
    """
    return np.array(size)


def gunzip(f_in: str, f_out: str) -> None:
    """
    Wrapper function around gunzip.

    Parameters:
    -----------
    f_in: str, file name of the gzip'ed file
    f_out: str: file name of the unzip'ed file

    Returns:
    --------
    None
    """
    with gzip.open(f_in, "rb") as f:
        with open(f_out, "wb") as o:
            shutil.copyfileobj(f, o)
    return None
