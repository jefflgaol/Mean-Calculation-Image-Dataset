# Mean-Calculation-Image-Dataset
This is a simple code to calculate the mean for an entire image dataset (per channel).

## How To Use
You can use the code like this:
```
python3 main.py \
  --image_directory='<path to image dataset>' \
  --image_format='<image extension>'
```
For example:
```
python3 main.py \
  --image_directory='images' \
  --image_format=png
```
After you run the code, it will show some result like this:
```
Blue: 81.21379842578362
Green: 82.72807018769504
Red: 84.30886060267338
```
