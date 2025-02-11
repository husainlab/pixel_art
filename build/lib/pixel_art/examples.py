import pixel_art.pixels as pixels

def notes():
  img = pixels.Image(16, 14)
  img.add_row(0, 'magenta')
  img.add_row(1, 'magenta', 'magenta', 'magenta', 'magenta',
                 'magenta', 'magenta', 'black', 'black',
                 'black', 'black', 'black', 'black',
                 'black', 'black', 'black', 'magenta')
  img.add_row(2, 'magenta', 'magenta', 'magenta', 'magenta',
                 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(3, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'white', 'white',
                 'white', 'white', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(4, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'black',
                 'black', 'black', 'black', 'black',
                 'black', 'white', 'black', 'magenta')
  img.add_row(5, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(6, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(7, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(8, 'magenta', 'magenta', 'black', 'black',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'black', 'black',
                 'black', 'white', 'black', 'magenta')
  img.add_row(9, 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'black', 'magenta',
                 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(10, 'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta',
                  'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta')
  img.add_row(11, 'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta',
                  'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta')
  img.add_row(12, 'magenta', 'magenta', 'black', 'black',
                  'black', 'black', 'magenta', 'magenta',
                  'magenta', 'magenta', 'black', 'black',
                  'black', 'black', 'magenta', 'magenta')
  img.add_row(13, 'magenta')
  img.display()

# test your code here
if __name__ == '__main__':
  notes()