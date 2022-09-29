#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;
int sum_mat(Mat img)
{
	int tmp = 0; 
	for(int y = 0; y < img.size().width; y++)
		for(int x = 0; x < img.size().height; x++)
			tmp += img.at<Vec3b>(x, y)[0];
	return tmp;
}

void keren2d(Mat img,Mat ker, Mat *ud)
{
	int sum = sum_mat(ker);
	int ri = (ker.size().width-1)/2;
	int rk = (ker.size().height-1)/2;
	for(int y = ri; y < img.size().width; y++)
		for(int x = rk; x < img.size().height; x++)
			for(int z = 0; z < 3; z++)
			{
				int tal = 0;
				for(int i = -ri; i < ri+1; i++)
					for(int k = -rk; k < rk+1; k++)
						tal += ud->at<Vec3b>(x+i,y+k)[z]*ker.at<Vec3b>(i+ri,k+rk)[z];
				ud->at<Vec3b>(x, y)[z] = tal/sum;
			}
}

int main(int argc, char** argv )
{
    if ( argc != 3 )
    {
        printf("program <biled sti> <2. biled sti>\n");
        return -1;
    }
    Mat image, ker, ud, ker_slor;
    image = imread( argv[1], 1 );
    ud = imread( argv[1], 1 );
    ker = imread( argv[2], 1 );
    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    if ( !ker.data )
    {
        printf("No image data \n");
        return -1;
    }
	ker_slor = Mat(5, 5, CV_8UC3, Scalar(1, 1, 1));
	keren2d(image,ker_slor,&ud);
    imshow("Image", image);
    imshow("ker_slor", ker_slor);
    imshow("slor", ud);
    imshow("keren", ker);
	keren2d(image,ker,&ud);
	imshow("ud", ud);
    waitKey(0);
    waitKey(0);
    waitKey(0);
    return 0;
}
