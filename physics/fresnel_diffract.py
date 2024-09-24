"""
Title: Fresnel Diffraction for Coherent and Monochromatic
        Wave Fields

Fresnel Diffraction describes the behavior of a wave field as it
moves through free space or interacts with an object under the
small angle approximation. It is particularly useful for near
field diffraction.

The following algorithm is an adaptation of the 'transfer function'
based approach contained in the reference. It is critically
sampled when:
pixel_size = wavelength * prop_dist / side_length

Or equivalently:
pixel_size = sqrt(wavelength * prop_dist / pixel_num)

Under and oversampling occur when the left-hand side is less
than or greater than the right-hand side, respectively.

This code is adapted and modified from:
Computational Fourier Optics: A MATLAB Tutorial by David Voelz
"""

from math import pi

import numpy as np
from scipy.fft import fft, fft2, fftshift, ifft, ifft2, ifftshift


def fresnel_diffract(wavefunc0, pixel_size, wavelength, prop_dist):
    """
    Fresnel Diffraction of 1D or 2D Wave Fields.

    This function calculates the Fresnel diffraction of a
    given wave field, suitable for near field diffraction. The
    wave field is assumed to be coherent and monochromatic.

    Args:
        wavefunc0 (np.ndarray): The initial wave field at the unpropagated plane.
        pixel_size (float): The physical size of a pixel (or data point) at the
        unpropagated plane.
        wavelength (float): The wavelength of the wave field.
        prop_dist (float): The desired propagation distance.

    Raises:
        ValueError: If the input wave field is not 1D or 2D.

    Returns:
        np.ndarray: The wave field at the propagated plane.
    """

    if len(wavefunc0.shape) == 1:
        return _fresnel_diffract_1d(wavefunc0, pixel_size, wavelength, prop_dist)
    elif len(wavefunc0.shape) == 2:
        return _fresnel_diffract_2d(wavefunc0, pixel_size, wavelength, prop_dist)
    else:
        err_shape = wavefunc0.shape
        raise ValueError(f"Expected a 1D or 2D wavefield, but got {err_shape}")


def _fresnel_diffract_2d(wavefunc0, pixel_size, wavelength, prop_dist):
    """
    Fresnel Diffraction of 2D Wave Fields.

    This private function is called by 'fresnel_diffract' to handle the
    fresnel diffraction of 2D wave fields specifically.

    Args:
        wavefunc0 (np.ndarray): The initial 2D wave field at the unpropagated plane.
        pixel_size (float): The physical size of a pixel (or data point) at the
        unpropagated plane.
        wavelength (float): The wavelength of the wave field.
        prop_dist (float): The desired propagation distance.

    Returns:
        np.ndarray: The 2D wave field at the propagated plane.
    """
    pixel_num, _ = wavefunc0.shape
    side_length = pixel_num * pixel_size

    # Coordinates in Fourier space are proportionate to 1 / pixel_size
    f_x = np.arange(-1 / (2 * pixel_size), 1 / (2 * pixel_size), 1 / side_length)

    f_x2d, f_y2d = np.meshgrid(f_x, f_x)

    # Transfer function which models diffraction
    transferf = np.exp(-1j * np.pi * wavelength * prop_dist * (f_x2d**2 + f_y2d**2))
    transferf = fftshift(transferf)

    # Fourier space wave function at the unpropagated plane
    f_wavefunc0 = fft2(fftshift(wavefunc0))
    # Wave function at the propagated, or 'z' plane
    wavefuncz = ifftshift(ifft2(transferf * f_wavefunc0))

    return wavefuncz


def _fresnel_diffract_1d(wavefunc_0, pixel_size, wavelength, prop_dist):
    """
    Fresnel Diffraction of 1D Wave Fields.

    This private function is called by 'fresnel_diffract' to handle the
    fresnel diffraction of 1D wave fields specifically.

    Args:
        wavefunc0 (np.ndarray): The initial 1D wave field at the unpropagated plane.
        pixel_size (float): The physical size of a pixel (or data point) at the
        unpropagated plane.
        wavelength (float): The wavelength of the wave field.
        prop_dist (float): The desired propagation distance.

    Returns:
        np.ndarray: The 1D wave field at the propagated plane.
    """
    pixel_num = len(wavefunc_0)
    side_length = pixel_num * pixel_size
    fx = np.arange(-1 / (2 * pixel_size), 1 / (2 * pixel_size), 1 / side_length)
    transferf = np.exp(-1j * pi * wavelength * prop_dist * (fx**2))
    transferf = fftshift(transferf)

    f_wavefunc_0 = fft(fftshift(wavefunc_0))

    wavefunc_z = ifftshift(ifft(transferf * f_wavefunc_0))

    return wavefunc_z
