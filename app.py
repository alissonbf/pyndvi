import os
from osgeo import gdal

INPUT_FOLDER = 'ressources'
OUTPUT_FOLDER = 'ndvi'

def calc_ndvi(file_name):
    gtif = gdal.Open("{}/{}".format(INPUT_FOLDER, file_name))

    output_file = "{}/ndvi_{}".format(OUTPUT_FOLDER, file_name)

    geotiff = gdal.GetDriverByName('GTiff')
    output = geotiff.CreateCopy(output_file, gtif, 0)
    output = geotiff.Create(
       output_file,
       gtif.RasterXSize, gtif.RasterYSize,
       1,
       gdal.GDT_UInt16
    )

    # get the red and nir bands
    red = gtif.GetRasterBand(1).ReadAsArray(0, 0, gtif.RasterXSize, gtif.RasterYSize)
    nir = gtif.GetRasterBand(4).ReadAsArray(0, 0, gtif.RasterXSize, gtif.RasterYSize)

    ndvi = (nir - red)/(nir + red)
    output.GetRasterBand(1).WriteArray(ndvi)

def main():
    # read the files inside ressources folder
    for file_name in os.listdir(INPUT_FOLDER):
        calc_ndvi(file_name)

if __name__ == '__main__':
    main()
