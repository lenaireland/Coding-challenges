def boxBlur(image):
    """The pixels in the input image are represented as integers. The algorithm 
    distorts the input image in the following way: Every pixel x in the output 
    image has a value equal to the average value of the pixel values from the 
    3 × 3 square that has its center at x, including x itself. All the pixels 
    on the border of x are then removed.

    Return the blurred image as an integer, with the fractions rounded down."""

    num_rows = len(image)
    num_cols = len(image[0])
    
    new_image = []
    
    for r in range(num_rows - 2):
        new_image.append([])
        for c in range(num_cols - 2):
            new_image[r].append(int((image[r][c] + image[r+1][c] + image[r+2][c] +
                                   image[r][c+1] + image[r+1][c+1] + image[r+2][c+1] +
                                   image[r][c+2] + image[r+1][c+2] + image[r+2][c+2])/9))
    
    return new_image