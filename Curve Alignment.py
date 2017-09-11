import numpy
from numpy.core.umath_tests import inner1d


def mod_Hausdorff_distance(model_set, test_set):

    # Find pairwise distance
    D_mat = inner1d(model_set, model_set)[numpy.newaxis].T + inner1d(test_set, test_set) - 2 * (numpy.dot(model_set, test_set.T))
    # Calculating the forward HD: mean(min(each col))
    FHD = numpy.mean(numpy.min(D_mat, axis=1))
    # Calculating the reverse HD: mean(min(each row))
    RHD = numpy.mean(numpy.min(D_mat, axis=0))
    # Calculating mhd
    MHD = max(FHD, RHD)
    return MHD

def band_to_cloud(kpts,band):

    nband = band.ndim
    npts = band.ndim


    cloud = []
    for i in range(nband):
        cloud.extend([[x, y] for x, y in zip(kpts, band[i])])

    return numpy.array(cloud)

bandA = numpy.array([[1,2,3,4,5,6,7],[9,9,9,9,9,9,9],[0,0,0,0,0,0,0]])
bandB = numpy.array([[1,2,3,5,5,6,7],[9,9,9,9,9,9,9],[0,0,0,0,0,0,0]])
bandB = bandB+10
print(bandB)
kpts = numpy.array([1,2,3,4,5,6,7])

print(1/(0.1+mod_Hausdorff_distance(band_to_cloud(kpts,bandB),band_to_cloud(kpts,bandA))))

