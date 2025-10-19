"""
Color Augmentation Module
Provides various color space augmentation techniques for computer vision tasks.
"""

import numpy as np
import cv2
from typing import Tuple, Optional, Union


class ColorAugmentation:
    """
    A collection of color augmentation techniques for image preprocessing.
    """
    
    @staticmethod
    def brightness_adjustment(image: np.ndarray, 
                             factor: float = 1.0) -> np.ndarray:
        """
        Adjust image brightness.
        
        Args:
            image: Input image (BGR or RGB)
            factor: Brightness factor (0.0 = black, 1.0 = original, >1.0 = brighter)
            
        Returns:
            Brightness adjusted image
        """
        if factor < 0:
            raise ValueError("Brightness factor must be non-negative")
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[:, :, 2] = np.clip(hsv[:, :, 2] * factor, 0, 255)
        return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    
    @staticmethod
    def contrast_adjustment(image: np.ndarray, 
                           factor: float = 1.0) -> np.ndarray:
        """
        Adjust image contrast.
        
        Args:
            image: Input image (BGR or RGB)
            factor: Contrast factor (0.0 = gray, 1.0 = original, >1.0 = more contrast)
            
        Returns:
            Contrast adjusted image
        """
        if factor < 0:
            raise ValueError("Contrast factor must be non-negative")
        
        mean = np.mean(image, axis=(0, 1), keepdims=True)
        adjusted = mean + factor * (image - mean)
        return np.clip(adjusted, 0, 255).astype(np.uint8)
    
    @staticmethod
    def saturation_adjustment(image: np.ndarray, 
                             factor: float = 1.0) -> np.ndarray:
        """
        Adjust image saturation.
        
        Args:
            image: Input image (BGR or RGB)
            factor: Saturation factor (0.0 = grayscale, 1.0 = original, >1.0 = more saturated)
            
        Returns:
            Saturation adjusted image
        """
        if factor < 0:
            raise ValueError("Saturation factor must be non-negative")
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[:, :, 1] = np.clip(hsv[:, :, 1] * factor, 0, 255)
        return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    
    @staticmethod
    def hue_shift(image: np.ndarray, 
                  shift: int = 0) -> np.ndarray:
        """
        Shift the hue channel.
        
        Args:
            image: Input image (BGR or RGB)
            shift: Hue shift value (-180 to 180)
            
        Returns:
            Hue shifted image
        """
        if not -180 <= shift <= 180:
            raise ValueError("Hue shift must be between -180 and 180")
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv = hsv.astype(np.int16)
        hsv[:, :, 0] = (hsv[:, :, 0] + shift) % 180
        hsv = hsv.astype(np.uint8)
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    @staticmethod
    def color_jitter(image: np.ndarray,
                    brightness: Tuple[float, float] = (0.8, 1.2),
                    contrast: Tuple[float, float] = (0.8, 1.2),
                    saturation: Tuple[float, float] = (0.8, 1.2),
                    hue: Tuple[int, int] = (-20, 20)) -> np.ndarray:
        """
        Apply random color jittering (combines brightness, contrast, saturation, hue).
        
        Args:
            image: Input image (BGR or RGB)
            brightness: Range for brightness factor
            contrast: Range for contrast factor
            saturation: Range for saturation factor
            hue: Range for hue shift
            
        Returns:
            Color jittered image
        """
        # Random brightness
        b_factor = np.random.uniform(brightness[0], brightness[1])
        image = ColorAugmentation.brightness_adjustment(image, b_factor)
        
        # Random contrast
        c_factor = np.random.uniform(contrast[0], contrast[1])
        image = ColorAugmentation.contrast_adjustment(image, c_factor)
        
        # Random saturation
        s_factor = np.random.uniform(saturation[0], saturation[1])
        image = ColorAugmentation.saturation_adjustment(image, s_factor)
        
        # Random hue
        h_shift = np.random.randint(hue[0], hue[1])
        image = ColorAugmentation.hue_shift(image, h_shift)
        
        return image
    
    @staticmethod
    def gamma_correction(image: np.ndarray, 
                        gamma: float = 1.0) -> np.ndarray:
        """
        Apply gamma correction.
        
        Args:
            image: Input image (BGR or RGB)
            gamma: Gamma value (< 1.0 = brighter, > 1.0 = darker)
            
        Returns:
            Gamma corrected image
        """
        if gamma <= 0:
            raise ValueError("Gamma must be positive")
        
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255 
                         for i in range(256)]).astype(np.uint8)
        return cv2.LUT(image, table)
    
    @staticmethod
    def histogram_equalization(image: np.ndarray, 
                              clip_limit: float = 2.0,
                              tile_grid_size: Tuple[int, int] = (8, 8)) -> np.ndarray:
        """
        Apply CLAHE (Contrast Limited Adaptive Histogram Equalization).
        
        Args:
            image: Input image (BGR or RGB)
            clip_limit: Threshold for contrast limiting
            tile_grid_size: Size of grid for histogram equalization
            
        Returns:
            Equalized image
        """
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
        lab[:, :, 0] = clahe.apply(lab[:, :, 0])
        return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    
    @staticmethod
    def channel_shuffle(image: np.ndarray) -> np.ndarray:
        """
        Randomly shuffle color channels.
        
        Args:
            image: Input image (BGR or RGB)
            
        Returns:
            Channel shuffled image
        """
        channels = list(cv2.split(image))
        np.random.shuffle(channels)
        return cv2.merge(channels)
    
    @staticmethod
    def grayscale_conversion(image: np.ndarray, 
                            keep_channels: bool = True) -> np.ndarray:
        """
        Convert image to grayscale.
        
        Args:
            image: Input image (BGR or RGB)
            keep_channels: If True, return 3-channel grayscale, else single channel
            
        Returns:
            Grayscale image
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if keep_channels:
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        return gray
    
    @staticmethod
    def color_cast(image: np.ndarray,
                  red_shift: int = 0,
                  green_shift: int = 0,
                  blue_shift: int = 0) -> np.ndarray:
        """
        Apply color cast by shifting individual channels.
        
        Args:
            image: Input image (BGR)
            red_shift: Shift for red channel (-255 to 255)
            green_shift: Shift for green channel (-255 to 255)
            blue_shift: Shift for blue channel (-255 to 255)
            
        Returns:
            Color cast image
        """
        result = image.astype(np.int16)
        result[:, :, 0] = np.clip(result[:, :, 0] + blue_shift, 0, 255)
        result[:, :, 1] = np.clip(result[:, :, 1] + green_shift, 0, 255)
        result[:, :, 2] = np.clip(result[:, :, 2] + red_shift, 0, 255)
        return result.astype(np.uint8)
    
    @staticmethod
    def temperature_tint(image: np.ndarray,
                        temperature: float = 0.0,
                        tint: float = 0.0) -> np.ndarray:
        """
        Adjust color temperature and tint.
        
        Args:
            image: Input image (BGR)
            temperature: Temperature adjustment (-1.0 to 1.0, negative = cooler, positive = warmer)
            tint: Tint adjustment (-1.0 to 1.0, negative = green, positive = magenta)
            
        Returns:
            Adjusted image
        """
        result = image.astype(np.float32)
        
        # Temperature: affect blue and red channels
        if temperature > 0:  # Warmer
            result[:, :, 2] = np.clip(result[:, :, 2] * (1 + temperature * 0.3), 0, 255)
            result[:, :, 0] = np.clip(result[:, :, 0] * (1 - temperature * 0.3), 0, 255)
        else:  # Cooler
            result[:, :, 0] = np.clip(result[:, :, 0] * (1 - temperature * 0.3), 0, 255)
            result[:, :, 2] = np.clip(result[:, :, 2] * (1 + temperature * 0.3), 0, 255)
        
        # Tint: affect green channel
        result[:, :, 1] = np.clip(result[:, :, 1] * (1 + tint * 0.3), 0, 255)
        
        return result.astype(np.uint8)
    
    @staticmethod
    def posterize(image: np.ndarray, 
                  levels: int = 4) -> np.ndarray:
        """
        Reduce the number of color levels (posterization effect).
        
        Args:
            image: Input image (BGR or RGB)
            levels: Number of color levels per channel (2-8)
            
        Returns:
            Posterized image
        """
        if not 2 <= levels <= 8:
            raise ValueError("Levels must be between 2 and 8")
        
        step = 256 // levels
        result = (image // step) * step
        return result.astype(np.uint8)
    
    @staticmethod
    def solarize(image: np.ndarray, 
                threshold: int = 128) -> np.ndarray:
        """
        Apply solarization effect (invert pixels above threshold).
        
        Args:
            image: Input image (BGR or RGB)
            threshold: Threshold value (0-255)
            
        Returns:
            Solarized image
        """
        result = image.copy()
        mask = result >= threshold
        result[mask] = 255 - result[mask]
        return result
    
    @staticmethod
    def random_color_augmentation(image: np.ndarray,
                                 probability: float = 0.5) -> np.ndarray:
        """
        Apply a random color augmentation with given probability.
        
        Args:
            image: Input image (BGR or RGB)
            probability: Probability of applying augmentation
            
        Returns:
            Augmented or original image
        """
        if np.random.random() > probability:
            return image
        
        augmentations = [
            lambda img: ColorAugmentation.brightness_adjustment(img, np.random.uniform(0.7, 1.3)),
            lambda img: ColorAugmentation.contrast_adjustment(img, np.random.uniform(0.7, 1.3)),
            lambda img: ColorAugmentation.saturation_adjustment(img, np.random.uniform(0.7, 1.3)),
            lambda img: ColorAugmentation.hue_shift(img, np.random.randint(-30, 30)),
            lambda img: ColorAugmentation.gamma_correction(img, np.random.uniform(0.7, 1.3)),
        ]
        
        aug_func = np.random.choice(augmentations)
        return aug_func(image)


# Example usage and demonstration
if __name__ == "__main__":
    # Create a sample image or load your own
    # img = cv2.imread('your_image.jpg')
    
    # For demonstration, create a synthetic image
    img = np.random.randint(0, 255, (300, 300, 3), dtype=np.uint8)
    
    augmenter = ColorAugmentation()
    
    # Apply various augmentations
    bright = augmenter.brightness_adjustment(img, factor=1.3)
    contrast = augmenter.contrast_adjustment(img, factor=1.5)
    saturated = augmenter.saturation_adjustment(img, factor=1.5)
    jittered = augmenter.color_jitter(img)
    gamma = augmenter.gamma_correction(img, gamma=1.5)
    equalized = augmenter.histogram_equalization(img)
    
    print("Color augmentation functions applied successfully!")
    print(f"Original shape: {img.shape}")
    print(f"Augmented shape: {jittered.shape}")