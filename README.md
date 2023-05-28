Sudoku Image Solver
    Video Demo: https://youtu.be/KBmzEk3-0xo
    Description:
        My project is a program that uses tensorflow's keras and backtracking to solve sudoku puzzles from images. 
        model.py: Uses tensor keras library and images made from number_image and rotate to create a weell trained model to detect typed numbers from an image. It includes five convolutional layers, which would be considered a lot for a model but it is needed at fonts have many different looks and filters are needed simplify the images for the computer to better understand them. I used this to save the model to nums.h5, which would be used later to predict the numbers in the sudoku puzzle.

        number_image.py: Takes fonts from the fonts file and creates images numbered 1-9 for each font.

        predict.py: Includes three helper functions to be used to read the numbers;
            predict_image: takes in a model and an image and predicts the number in the image using nums.h5. Returns the index with the highest number.

            trim: Takes the top left pixel and trims that color until a far different color is detected. When one image is given, the function returns the image trimmed. When two images are given, the first image gives a box where that image would be trimmed and that box is applied to the second image, also returning the box.

            predict: Takes in a filename and opens the file as a cv2 array in size 28, 28 and determines whether the image is all or mostly white, where the function would return 0 as the image would be a blank space in a sudoku puzzle. Else, the function would return the return value from the predict_image function.

        rotate.py: For each image saved from number_image.py, the program first rotates each image 5 degrees counter-clockwise and clockwise then, to create the largest and different dataset for the model to train on, each image are slightly different from each other in terms of positioning.

        solver.py: A class that uses backtracking to solve a grid of a sudoku puzzle.
            possible: Checks given a number, row and column if the number would have any problems with the sudoku rules. Return True if so, False if not.

            check: Checks if a sudoku grid is correctly solved.

            solve: Iterating through each cell of the grid, if a cell is empty, the fucntion iterates through 1-9 and uses possible to check if the number would be correct in that position. The function then returns solve, recursively backtracking the problem until the grid is solved with checking with check. If all 1-9 doesn't work, then you know that the previous number you put in doesn't work and now have to take that out. I was stuck here for a decently long time because I was wondering why the function wasn't return a correctly solved grid but I remebered that you couldn't assign a matrix to a variable without it changing unless you use deepcopy from the copy library.

        sudoku_reader.py's reader: Takes in a filename where the sudoku puzzle is stored and changes the image to black and white so that the image would be trimmed with less trouble. The image is then trimmed so that only the corners of the sudoku puzzle are the corners of the image. Then, using PIL's Image, you would crop each cell of the sudoku puzzle and predict it with predict.py, stroing the values in a grid and finally returning the grid.

        sudoku.py: Takes in using commandline a folder or a file containing the images and a folder where the images with the solutions are shown. First, the images are processed in sudoku_reader.py, where a grid is returned. Then, using Solver, a solved version of the grid is returned. For each empty cell in the original picture, a solved and correct number is placed there. The resulting image is then saved to the out folder.

        This project can definetly be expanded and have its limitations. I can see having this as an app or extension in chrome. Limitations of this project include not being able to detect a sudoku puzzle when the top left pixel is different so that the puzzle isn't trimmed correctly and another problem is when the puzzle is too small and there is not enough information for the comuter to read. The most time consuming part of the project was cleaning and creating the data and waiting for the model the train.
