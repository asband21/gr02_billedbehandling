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

void deliesen(Mat img, Mat *ud, int r)
{
	for(int y = r; y < img.size().width-r; y++)
		for(int x = r; x < img.size().height-r; x++)
		{
			bool tal = false;
			for(int i = -r; i < r+1 && !tal; i++)
				for(int k = -r; k < r+1 && !tal; k++)
					if(img.at<Vec3b>(x+i,y+k)[0] > 0)
						tal = true;
			ud->at<Vec3b>(x, y)[0] = tal*255;
			ud->at<Vec3b>(x, y)[1] = tal*255;
			ud->at<Vec3b>(x, y)[2] = tal*255;
		}
}

void erosien(Mat img, Mat *ud, int r)
{
	for(int y = r; y < img.size().width-r; y++)
		for(int x = r; x < img.size().height-r; x++)
		{
			bool tal = true;
			for(int i = -r; i < r+1; i++)
				for(int k = -r; k < r+1; k++)
					if(img.at<Vec3b>(x+i,y+k)[0] == 0)
						tal = false;
			ud->at<Vec3b>(x, y)[0] = tal*255;
			ud->at<Vec3b>(x, y)[1] = tal*255;
			ud->at<Vec3b>(x, y)[2] = tal*255;
		}
}

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("program <biled sti> <2. biled sti>\n");
        return -1;
    }
    Mat img,img_grå,range,ero , del,clos,ope;
    img = imread( argv[1], 1 );
	cvtColor(img, img_grå ,COLOR_BGR2GRAY);
	cvtColor(img, range, COLOR_BGR2GRAY);
	cvtColor(img, del, COLOR_BGR2GRAY);
	cvtColor(img, ero, COLOR_BGR2GRAY);
	cvtColor(img, del, COLOR_BGR2GRAY);
	cvtColor(img, del, COLOR_BGR2GRAY);
    //ud = imread( argv[1], 1 );
    if ( !img.data )
    {
        printf("No image data \n");
        return -1;
    }

	inRange(img_grå,0 , 90, range);
	//deliesen(range, &del,1);
	erosien(range, &del,2);
    imshow("img", img);
    imshow("img_grå", img_grå);
    imshow("del", del);
    imshow("range", range);
	//Mat *low = new Mat(img.rows, img.cols, img.type(), 0);
	//Mat *high = new Mat(img.rows, img.cols, img.type(), 150);
	// You can try more different parameters
	//ud = inRange(img, Scalar(0), Scalar(150), ud);
	//threshold(img, ud,0,50, THRESH_BINARY_INV); 
    waitKey(0);
    return 0;
}
