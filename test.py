import shutil, os
from common_ops import *

from rentool import load_image, save_image

def test_load_and_save():
    img = load_image('test_imgs/walk_anim_background.png')
    save_image(img, 'deleteme.png')
    os.remove('deleteme.png')

def test_transparent_overlay():
    subject = load_image('test_imgs/walk_anim_subject/0001.png')
    background = load_image('test_imgs/walk_anim_background.png')
    result = transparentOverlay(subject, background)
    expected = load_image('test_imgs/walk_anim_expected/0001.png')
    assert result.all() == expected.all()

def test_foreground_extract():
    full_image = load_image('test_imgs/walk_anim_expected/0001.png')
    background = load_image('test_imgs/walk_anim_background.png')
    threshold = 8
    result = extract_foreground(full_image, background, threshold)
    expected = load_image('test_imgs/fg-extract-expected.png')
    assert result.all() == expected.all()

def test_blend():
    img1 = load_image('test_imgs/walk_anim_expected/0001.png')
    img2 = load_image('test_imgs/walk_anim_expected/0005.png')
    result = blend(img1, img2)
    expected = load_image('test_imgs/blend_expected.png')
    assert result.all() == expected.all()

def test_denoise():
    img1 = load_image('test_imgs/noisy_background.png')
    fastNL = denoise(img1, 10, mode='fastNL')
    expected = load_image('test_imgs/fastNL_denoised.png')
    assert fastNL.all() == expected.all()
    median = denoise(img1, 10, mode='median')
    expected = load_image('test_imgs/median_denoised.png')
    assert median.all() == expected.all()

def test_scale():
    raise NotImplementedError()

def test_interpolation():
    raise NotImplementedError()

def test_add_noise():
    raise NotImplementedError()

def test_diff():
    raise NotImplementedError()