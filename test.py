# from numpy.core.umath_tests import inner1d
# import numpy
#
# A = numpy.array([[1,2],[3,4],[5,6],[6,7]])
# B = numpy.array([[1,2],[3,4],[5,6],[7,8],[7,9]])
#
# # print(numpy.shape(A))
# kpts = numpy.array([0,0.1,0.2,0.3,0.4,0.5])
# band = numpy.array([[1,2,3,4,5,6],[9,9,9,9,9,9]])
# nband  = band.ndim
# npts = band.size/band.ndim
# print(nband, npts)
# print(npts,nband,len(kpts))
# cloud = numpy.array([])
# for i in range(nband):
#
# print(cloud)
#
# # D_mat = numpy.sqrt(inner1d(A, A)[numpy.newaxis].T + inner1d(B, B) - 2 * (numpy.dot(A, B.T)))
# # print(inner1d(A, A)[numpy.newaxis].T)
# # print(inner1d(B, B))
# # print('+',inner1d(A, A)[numpy.newaxis].T + inner1d(B, B))
# # print((numpy.dot(A, B.T)))
# # print(D_mat)
# # print(numpy.mean(numpy.min(D_mat, axis=0)),numpy.min(D_mat, axis=1))#),numpy.min(D_mat, axis=2),numpy.min(D_mat, axis=3))